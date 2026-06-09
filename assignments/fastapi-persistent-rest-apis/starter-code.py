import sqlite3
from typing import Optional

from fastapi import FastAPI, HTTPException, Header, Request
from pydantic import BaseModel

app = FastAPI()
DB_PATH = "books.db"
API_KEY = "school-api-key"

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.on_event("startup")
def startup_event():
    initialize_db()


@app.get("/")
async def root():
    return {"message": "FastAPI persistent Books API is running."}


def verify_api_key(api_key: Optional[str]):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


@app.get("/books/")
async def read_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, year FROM books")
    rows = cursor.fetchall()
    conn.close()
    return [Book(**dict(row)) for row in rows]


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, year FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Book(**dict(row))


@app.post("/books/")
async def create_book(book: BookCreate, x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (book.title, book.author, book.year),
    )
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    return {"id": book_id, **book.dict()}


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: BookUpdate, x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM books WHERE id = ?", (book_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")

    updates = []
    values = []
    if book.title is not None:
        updates.append("title = ?")
        values.append(book.title)
    if book.author is not None:
        updates.append("author = ?")
        values.append(book.author)
    if book.year is not None:
        updates.append("year = ?")
        values.append(book.year)

    if not updates:
        conn.close()
        raise HTTPException(status_code=400, detail="No fields to update")

    values.append(book_id)
    cursor.execute(f"UPDATE books SET {', '.join(updates)} WHERE id = ?", tuple(values))
    conn.commit()
    conn.close()
    return {"message": "Book updated"}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int, x_api_key: Optional[str] = Header(None)):
    verify_api_key(x_api_key)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}


@app.get("/books/search/")
async def search_books(author: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if author:
        cursor.execute(
            "SELECT id, title, author, year FROM books WHERE LOWER(author) = LOWER(?)",
            (author,),
        )
    else:
        cursor.execute("SELECT id, title, author, year FROM books")
    rows = cursor.fetchall()
    conn.close()
    return {"results": [Book(**dict(row)) for row in rows]}
