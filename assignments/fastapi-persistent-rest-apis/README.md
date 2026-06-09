# 📘 Assignment: Persistent REST APIs with FastAPI

## 🎯 Objective

Build a FastAPI application that stores data in SQLite and supports RESTful CRUD operations. Practice request validation, database persistence, and API search.

## 📝 Tasks

### 🛠️ Set up the FastAPI application

#### Description
Create a new FastAPI app and configure a SQLite database connection.

#### Requirements
Completed program should:

- Import `FastAPI`, `Request`, and `HTTPException` from `fastapi`.
- Initialize a database connection and create a `books` table if it does not exist.
- Create a root route (`GET /`) that returns a welcome JSON message.
- Ensure the app can be run with `uvicorn starter-code:app --reload`.

### 🛠️ Create persistent CRUD endpoints

#### Description
Add routes for creating, reading, updating, and deleting books in the SQLite database.

#### Requirements
Completed program should:

- Add `GET /books/` to return all books.
- Add `GET /books/{book_id}` to return a book by its ID.
- Add `POST /books/` to create a new book record.
- Add `PUT /books/{book_id}` to update an existing book.
- Add `DELETE /books/{book_id}` to remove a book.
- Return `404` when a specific book is not found.

### 🛠️ Validate input with Pydantic models

#### Description
Use Pydantic models to validate request bodies for book data.

#### Requirements
Completed program should:

- Define a `BookCreate` model for incoming `POST` requests.
- Define a `BookUpdate` model for updates.
- Validate that `title`, `author`, and `year` are present and correctly typed.
- Return the created or updated book as JSON.

### 🛠️ Add search and API key protection

#### Description
Extend the API with a query search endpoint and a simple API key header check.

#### Requirements
Completed program should:

- Add `GET /books/search/` that accepts an optional `author` query parameter.
- Filter books by author when the query parameter is provided.
- Require an `X-API-Key` header for all modifying routes (`POST`, `PUT`, `DELETE`).
- Return a `401` error if the API key is missing or invalid.
