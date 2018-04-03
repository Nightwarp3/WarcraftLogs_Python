from flask import Flask, request, render_template

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
    return render_template('charrank.html', display="none")

@app.route('/char_rank/', methods=['GET', 'POST'])
def getCharRank():
    name = request.args.get('nameField')
    server = request.args.get('serverField')
    region = request.args.get('Region')

    validate_name(name)
    rank_json = la.getCharacterRanking(name, server, region)


    return render_template('charrank.html', display="normal")

def validate_name(name):
    test = "hello"
    if test.isalpha():
        return True
    else:
        error_msg = 'Name entered, "' + name + '" is invalid. Please correct and try again.'
        raise Exception(error_msg)

if __name__ == "__main__":
    app.debug = True
    app.run()
