from project import main
from flask import Flask

app = Flask(__name__)

@app.route('/')
def app():
  return main.app()
