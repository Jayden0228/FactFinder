from flask import Flask, render_template, request
from app.ML import ml
from app.Scrapping import Scrape

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/input', methods=['POST'])
def Input():
    if request.method == 'POST':
        btn=request.form['btntype']

        if btn=='headline':
            return render_template("input.html", header='News Headline')
        elif btn=='article':
            return render_template("input.html", header='News Article Link')
            

    # return render_template("input.html")

@app.route('/result')
def Result():
    return render_template("result.html")


if __name__=='__main__':
    app.run(debug=True)
