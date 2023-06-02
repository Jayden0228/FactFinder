from flask import Flask, render_template, request
from mL.ml import fake_news
from scrapping.Scrape import getHeadline 

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/input', methods=['POST'])
def Input():
    if request.method == 'POST':
        btn=request.form['btntype']

        if btn=='headline':
            return render_template("input.html", header='News Headline', value='Headline')
        elif btn=='article':
            return render_template("input.html", header='News Article Link', value='Article')
            

    # return render_template("input.html")

@app.route('/result', methods=['POST'])
def Result():
    if request.method == 'POST':
        texttype=request.form['texttype']
        
        if texttype=='Headline':
            res=fake_news(request.form['textbox'])
            
            if res=="REAL":
                src='../static/Images/real.png'
                res="REAL"
                return render_template("result.html", src=src, res=res)
            elif res=="FAKE":
                src='../static/Images/fake.png'
                res="FAKE"
                return render_template("result.html", src=src, res=res)
        
        elif texttype=='Article':
            con=getHeadline(request.form['textbox'])
            res=fake_news(con)

            if res=="REAL":
                src='../static/Images/real.png'
                res="REAL"
                return render_template("result.html", src=src, res=res)
            elif res=="FAKE":
                src='../static/Images/fake.png'
                res="FAKE"
                return render_template("result.html", src=src, res=res)
            
    return render_template("index.html")
        
    # return render_template("result.html")


if __name__=='__main__':
    app.run(debug=True)
