# FastAPI Social Network

A simple social network API built with FastAPI, SQLAlchemy, and PostgreSQL. This project was build to get closer to fastapi ecosystem.

## Features
- User registration, update, and deletion
- User friendship management (many-to-many relationships)
- Post creation, update, and deletion
- Retrieve user and post data
- PostgreSQL database with SQLAlchemy ORM

## Project Structure
```
app/
  ├── crud/           # CRUD operation modules
  ├── database/       # Database config and initialization
  ├── models/         # SQLAlchemy models
  ├── routers/        # FastAPI routers (endpoints)
  ├── schemas/        # Pydantic schemas
  └── main.py         # FastAPI application entrypoint
```

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd fastapi_socialnetwork
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your PostgreSQL database settings in `app/database/database.py`.

### Database Initialization
Tables are created automatically at startup using the `create_tables()` function.

### Running the Application
```bash
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API documentation (Swagger UI).

## API Overview
- **Users**: Register, update, delete, list, manage friendships
- **Posts**: Create, update, delete, list, get user posts

## License
This project is licensed under the MIT License.
