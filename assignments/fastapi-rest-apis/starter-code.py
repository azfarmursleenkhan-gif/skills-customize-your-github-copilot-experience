from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

books: List[Book] = [
    Book(id=1, title="The Python Journey", author="A. Student", year=2023),
    Book(id=2, title="Learning FastAPI", author="B. Developer", year=2024),
]

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Books API!"}

@app.get("/books/")
async def read_books():
    return books

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/")
async def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books/search/")
async def search_books(author: Optional[str] = None):
    if author:
        filtered = [book for book in books if book.author.lower() == author.lower()]
        return {"results": filtered}
    return {"results": books}
