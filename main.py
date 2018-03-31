from flask import Flask
from flask import render_template
from WarcraftLogsPython import LogsAPIRequests as la

app = Flask(__name__)

@app.route('/')
def MainPage():
    return render_template('MainWebPage.html')

@app.route('/getChar')
def get_char():
    character = la.getCharacterRanking()

if __name__ == "__main__":
    app.run()