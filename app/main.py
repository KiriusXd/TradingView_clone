# app/main.py
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


if __name__ == "__main__":
    server_thread = Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()
    open_browser()
