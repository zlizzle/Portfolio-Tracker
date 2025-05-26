from fastapi import FastAPI
from sqlmodel import SQLModel
from .database import engine
from .routers.portfolio import router as portfolio_router

#Create the FastAPI “app” instance
app = FastAPI(title="Portfolio Tracker")

#on startup, create any database tables that don’t yet exist
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

#Mount the portfolio router under the /assets prefix
app.include_router(portfolio_router, prefix="/assets", tags=["assets"])
