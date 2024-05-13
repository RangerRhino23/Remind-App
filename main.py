from flask import Flask, render_template, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


app.run('localhost',25565)