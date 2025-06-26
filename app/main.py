from fastapi import FastAPI
import os
import asyncpg

app = FastAPI()

@app.on_event("startup")
async def startup():
    db_url = os.getenv("DATABASE_URL")
    try:
        conn = await asyncpg.connect(db_url)
        await conn.close()
        print("✅ Connected to PostgreSQL!")
    except Exception as e:
        print("❌ Database connection failed:", e)

@app.get("/")
def read_root():
    return {"message": "FastAPI + Docker + PostgreSQL"}

