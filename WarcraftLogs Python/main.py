from flask import Flask
from flask import render_template
import LogsAPIRequests as la
import MySqlRequests as mydb

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('MainWebPage.html')

@app.route('/#')
def


if __name__ == '__main__':
    app.run()

