# app/main.py
from app.api.endpoints import market_data  # Импорт роутера
from app.services.database import init_db
from app.core.config import logger
import logging
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import webbrowser
import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import tkinter as tk
from threading import Thread

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)


def open_browser():
    root = tk.Tk()
    root.title("TradingView Analog")
    label = tk.Label(root, text="Сервер запущен. Откройте http://localhost:8000 в браузере.")
    label.pack(padx=20, pady=20)
    root.mainloop()


# start.py

# Инициализация приложения
app = FastAPI()
app.include_router(market_data.router)  # Подключение эндпоинтов
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Инициализация БД
init_db()


@app.on_event("startup")
async def startup():
    logger.info("Сервер запущен")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Сервер остановлен")


@app.get("/")
async def root(request: Request):
    logger.info("Запрос к главной странице")
    return templates.TemplateResponse("index.html", {"request": request})

# ... остальной код запуска сервера и GUI ...
if __name__ == "__main__":
    server_thread = Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    open_browser()
