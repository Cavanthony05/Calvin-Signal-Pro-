from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated database
users = {
    "calvin": {"password": "1234", "role": "premium"}
}

# Simulated signal generator
def generate_signal(user_type):
    directions = ["BUY", "SELL"]
    assets = ["EUR/USD", "GBP/JPY", "USD/JPY", "BTC/USD"]
    timeframes = ["1m", "5m", "15m"]
    confidence = random.randint(80, 99) if user_type == "premium" else random.randint(60, 75)

    return {
        "signal": random.choice(directions),
        "asset": random.choice(assets),
        "timeframe": random.choice(timeframes),
        "confidence": f"{confidence}%",
        "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") + " UTC"
    }

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in users and users[uname]['password'] == pwd:
            session['user'] = uname
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in users:
            error = 'Username already exists'
        else:
            users[uname] = {"password": pwd, "role": "basic"}
            return redirect(url_for('login'))
    return render_template('register.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = session['user']
    role = users[user]['role']
    signal = generate_signal(role)
    return render_template('dashboard.html', signal=signal, user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
