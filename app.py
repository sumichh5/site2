from flask import Flask, redirect
import threading
import os
import bot  # импорт твоего файла

app = Flask(__name__)

# 🔥 запускаем бот в отдельном потоке
threading.Thread(target=bot.main).start()

@app.route('/')
def index():
    return redirect("https://discord.gg/2cU2wynKK")

port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)
