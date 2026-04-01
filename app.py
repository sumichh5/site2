from flask import Flask
import subprocess

app = Flask(__name__)

# 🔥 запускаем бот ОДИН раз при старте
subprocess.Popen(["python", "bot.py"])

@app.route('/')
def index():
    return """
    <h1>Мой сайт работает 🚀</h1>
    <p>Бот уже запущен</p>
    """

# Railway даёт порт через переменную
import os
port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)
