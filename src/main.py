import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.app.routes import router
from src.database import test_database_connection

app = FastAPI(
    title="Expense Tracker API",
    description="This is a simple Expense Tracker API built with FastAPI.",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    if test_database_connection():
        print("✅ Database connected successfully!")
    else:
        print("❌ Database connection failed!")


START_TIME = time.monotonic()


@app.get("/")
async def read_root():
    uptime_seconds = time.monotonic() - START_TIME
    return JSONResponse(
        content={
            "status": "success",
            "message": "Welcome to the FastAPI application!",
            "uptime": int(uptime_seconds),
        }
    )


@app.get("/health")
async def health_check():
    uptime_seconds = time.monotonic() - START_TIME
    return JSONResponse(
        content={
            "status": "success",
            "message": "The application is healthy!",
            "uptime": int(uptime_seconds),
        }
    )


app.include_router(
    router,
)
