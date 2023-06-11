import requests
from bs4 import BeautifulSoup

channelTag={
    'heraldgoa': 'h2',
    'indianexpress': 'h1',
    'indiatimes': 'h1',
    'ndtv': 'h1',
    'hindustantimes': 'h1',
    'thehindu': 'h1',
    'indiatoday': 'h1',
    'cnn': 'h1',
    'bbc': 'h1',
    'snopes': 'h1'
}

def getTag(s):
    l=s.split('.')
    if('https://indianexpress' in l):
        return channelTag['indianexpress']
    else:
        return channelTag[l[1]]


def getHeadline(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag=getTag(url)
    headlines = soup.find('body').find(tag)
    return headlines.text.strip()

# print(getHeadline('https://www.heraldgoa.in/News-Today/Gang-of-robbers-attempt-three-robberies-shoot-at-Police/205312'))