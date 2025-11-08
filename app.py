import os
from flask import Flask, render_template

app = Flask(__name__)  # <-- должно быть app

# === Тут твой код ===

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # <-- debug=False