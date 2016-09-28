from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/create')
def create_form():
    today = date.today()
    return render_template('create.html', today=today)