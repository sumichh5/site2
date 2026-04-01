from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://discord.gg/2cU2wynKK")

port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)
