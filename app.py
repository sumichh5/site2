from flask import Flask, redirect
import subprocess
import os

app = Flask(__name__)

# 🔥 запуск бота при старте
subprocess.Popen(["python", "bot.py"])

@app.route('/')
def index():
    return redirect("https://discord.gg/2cU2wynKK")  # сюда можешь вставить свой сервер

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
