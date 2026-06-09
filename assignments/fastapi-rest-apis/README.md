# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework, including routing, request handling, validation, and JSON responses.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a new FastAPI app and create a file called `main.py`.

#### Requirements
Completed program should:

- Import `FastAPI` from `fastapi`.
- Create an app instance with `app = FastAPI()`.
- Define at least one root route (`GET /`) that returns a JSON welcome message.
- Run the app using `uvicorn`.

### 🛠️ Build CRUD-style Routes

#### Description
Add endpoints for managing a list of books. Each book should include an `id`, `title`, `author`, and `year`.

#### Requirements
Completed program should:

- Add a route to return all books: `GET /books/`.
- Add a route to return a single book by ID: `GET /books/{book_id}`.
- Return a `404` response if a book ID is not found.

### 🛠️ Validate Input Data

#### Description
Use Pydantic models to validate incoming request data for creating and updating books.

#### Requirements
Completed program should:

- Define a `Book` model using `pydantic.BaseModel`.
- Add a route to create a new book: `POST /books/`.
- Accept JSON request data and return the created book.
- Add proper validation for required fields.

### 🛠️ Add Query Parameters and Response Structure

#### Description
Extend your API with optional query parameters and consistent JSON responses.

#### Requirements
Completed program should:

- Add a route `GET /books/search/` that accepts an optional `author` query parameter.
- Filter books by author when the query parameter is provided.
- Return a JSON object with a key named `results` containing the list of books.

## 💡 Getting Started

Install required packages before running the app:

```bash
pip install fastapi uvicorn
```

Run the app locally:

```bash
uvicorn starter-code:app --reload
```
