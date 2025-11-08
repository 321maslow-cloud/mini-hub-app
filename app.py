from flask import Flask, render_template

app = Flask(__name__)

# === Главная страница (хаб) ===
@app.route('/')
def index():
    return render_template('index.html')

# === Страница КриптоТрекера ===
@app.route('/crypto')
def crypto():
    return render_template('crypto.html')

# === Страница Новостей ===
@app.route('/news')
def news():
    return render_template('news.html')

# === Страница Профиля ===
@app.route('/profile')
def profile():
    return render_template('profile.html')