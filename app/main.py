from fastapi import FastAPI
from sqlmodel import SQLModel
from .database import engine
from .routers.portfolio import router as portfolio_router

app = FastAPI(title="Portfolio Tracker")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(portfolio_router, prefix="/assets", tags=["assets"])
