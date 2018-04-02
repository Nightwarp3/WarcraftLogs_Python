from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/report_results')
def report_results():
    return render_template('reportresults.html')

@app.route('/fight_results')
def fight_results():
    return render_template('fightresults.html')

@app.route('/char_rank')
def char_rank():
    return render_template('charrank.html')

if __name__ == "__main__":
    app.run()
