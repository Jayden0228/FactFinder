from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pickle

port_stem=PorterStemmer()
vect=TfidfVectorizer()

vector_form=pickle.load(open('vector.pkl','rb'))
load_model=pickle.load(open('model.pkl','rb'))

def stemming(content):
    con=re.sub('[^a-zA-Z]',' ',content)
    con=con.lower()
    con=con.split()
    con=[port_stem.stem(word) for word in con if not word in stopwords.words('english')]
    con=' '.join(con)
    return con

def fake_news(news):
    news=stemming(news)
    input_data=[news]
    vector_form1=vector_form.transform(input_data)
    prediction = load_model.predict(vector_form1)
    return prediction[0]