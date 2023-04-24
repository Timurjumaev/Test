import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.expense import expenses_router
from routes.incomes import incomes_router
from routes.phones import phones_router
from routes.tariifs import tariffs_router
from routes.users import users_router
from utils.login import login_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(phones_router)
app.include_router(tariffs_router)
app.include_router(incomes_router)
app.include_router(expenses_router)
app.include_router(login_router)
