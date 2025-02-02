# start.py
import threading
import tkinter as tk
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Импорты из вашего приложения
from app.services.database import init_db
from app.api.endpoints import market_data  # Импорт роутера
from app.core.config import logger  # Импорт логгера

# Инициализация FastAPI
app = FastAPI()

# Подключение CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение эндпоинтов
app.include_router(market_data.router)

# Статические файлы и шаблоны
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Инициализация базы данных


@app.on_event("startup")
async def startup_event():
    init_db()
    logger.info("Application startup: Database initialized")


@app.get("/")
async def root(request: Request):
    """Главная страница с графиком"""
    logger.info("Request to root endpoint")
    return templates.TemplateResponse("index.html", {"request": request})


def run_server():
    """Запуск сервера Uvicorn"""
    logger.info("Starting Uvicorn server...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_config=None  # Отключаем стандартное логирование Uvicorn
    )


def open_browser():
    """Открытие GUI с адресом"""
    root = tk.Tk()
    root.title("TradingView Analog")
    label = tk.Label(
        root,
        text="Сервер запущен. Откройте http://localhost:8000 в браузере.",
        padx=20,
        pady=20
    )
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    # Запуск сервера в отдельном потоке
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Открытие GUI с адресом
    try:
        open_browser()
    except Exception as e:
        logger.error(f"GUI error: {str(e)}")
    finally:
        logger.info("Application shutdown")
