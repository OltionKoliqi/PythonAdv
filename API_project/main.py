from fastapi import FastAPI
from routers import recipes, categories
import os
from dotenv import load_dotenv
from database import get_db_connection

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

app.include_router(categories.router)
app.include_router(recipes.router)

@app.on_event("startup")
def startup():
    conn = get_db_connection()
    cursor = conn.curosr()

    cursor.execute('''
        CREATE TABLE if NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE if NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            ingredients TEXT,
            cuisine TEXT,
            difficulty TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    ''')

    conn.commit()
    conn.close()

@app.get('/')
def read_root():
    return {"message": "FastAPI with SQLite project"}























