#from WarcraftLogsPython.main import app
from flask import Flask

app = Flask(__name__)

app.route('/')
def mainpage():
    return ('Helllflakjdf;aljef;lawfjasl;ef')

if __name__ == "__main__":
    app.run()
