# start.py
import webbrowser
import threading
import tkinter as tk
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from app.services.database import init_db

# Инициализация FastAPI
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Инициализация базы данных
init_db()


@app.get("/")
async def root(request: Request):
    """Главная страница с графиком"""
    return templates.TemplateResponse("index.html", {"request": request})


def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)


def open_browser():
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
    open_browser()
