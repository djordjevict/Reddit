CLIENT_ID = '7_XBLzur5GVXFz7Y25NsuQ'
SECRET_TOKEN = 'HzdUa_9xEzxKcMSb8kJD3VB0JMZg8g'

import requests
import pandas as pd
from textblob import TextBlob
import re

class RedditAuth():

    def authenticate(self):
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)
        data = {'grant_type': 'password',
        'username': 'Macupikcu',
        'password': 'SljivovicaRakija15'}
        headers = {'User-Agent': 'OurAPI/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
        TOKEN = res.json()['access_token']
        headers['Authorization'] = f'bearer {TOKEN}'
        return headers

class RedditAnalyze():

    def __init__(self):
        self.headers = RedditAuth().authenticate()

    def data_collection(self):                 
        res = requests.get('https://oauth.reddit.com/r/college', headers=self.headers, params={'limit':'20'})

        df = pd.DataFrame()

        for post in res.json()['data']['children']:
            temp = self.analyze_sentiment(post['data']['title'])
            df = df.append({
                'Author': post['data']['author'],
                'Title': post['data']['title'],
                'Selftext': post['data']['selftext'],
                'Sentiment': temp
            }, ignore_index=True)

        return df

    def analyze_sentiment(self, text):
        analysis = TextBlob(text)
               
        if analysis.polarity > 0:
            return "Positive post"
        elif analysis.polarity == 0:
            return "Neutral post"
        else:
            return "Negative post"
        

if __name__ == '__main__':

    reddit = RedditAnalyze()
    result = reddit.data_collection()               
    print(result)