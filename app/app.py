import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}