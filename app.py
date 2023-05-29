from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/input')
def Input():
    return render_template("input.html")

@app.route('/result')
def Result():
    return render_template("result.html")


if __name__=='__main__':
    app.run(debug=True)
