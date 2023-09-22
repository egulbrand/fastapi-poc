from fastapi import FastAPI
import os 
from pymongo.mongo_client import MongoClient
from routers.dosages import router as dosages_router
from routers.users import router as users_router
from auth.authentication import router as auth_router
from db.mongo_manager import MongoManager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Pill Agent Dev",
    summary="""An API for managing schedules, dosages and reporting
    for personal pharmaceutical use.""",
    version="Versioning is route and method dependent"
)

@app.on_event("startup")
def startup_db_client():
    MongoManager.getInstance()

@app.on_event("shutdown")
def shutdown_db_client():
    MongoManager.closeDB()

app.include_router(dosages_router, tags=["dosages"], prefix="/dosages")
app.include_router(users_router, tags=["users"], prefix="/users")
app.include_router(auth_router, tags=["authentication"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# @app.get("/", tags=["Group 1"])
# def root():
#     return "Hello World"