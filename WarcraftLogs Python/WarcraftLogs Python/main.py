from flask import flask

app = Flask(__name__)

@wrapper_descriptor.route('/')
def hello_world():
        return 'Hello, World!'

if __name__ == '__main__':
    app.run()

