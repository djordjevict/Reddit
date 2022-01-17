#CLIENT_ID='o6LqV4RYbHv8rnkMazt01g'
CLIENT_ID = '7_XBLzur5GVXFz7Y25NsuQ'
#SECRET_TOKEN='HWcRqlhlss5bz0I1Z3VJ1t2chg2p0Q'
SECRET_TOKEN = 'HzdUa_9xEzxKcMSb8kJD3VB0JMZg8g'

import requests
import pandas as pd

class RedditAuth():

    def authenticate(self):
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)
        #'grant_type': 'authorization_code'
        data = {'grant_type': 'password',
        'username': 'Macupikcu',
        'password': 'SljivovicaRakija15'}
        headers = {'User-Agent': 'OurAPI/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
        TOKEN = res.json()['access_token']
        headers['Authorization'] = f'bearer {TOKEN}'
        return headers

class Ostalo():

    def __init__(self):
        self.headers = RedditAuth().authenticate()

    def nekaFunkcija(self):                 # stavi /porn umesto /python, ja kazem, Reddit beskonacna stvar...
        res = requests.get('https://oauth.reddit.com/r/python/hot', headers=self.headers, params={'limit':'10'})

        df = pd.DataFrame()

        for post in res.json()['data']['children']:
            #print(post['data'].keys())     # Da prikaze sve moguce kljuceve po kojima mozemo da izvlacimo podatke
            df = df.append({
                'Title': post['data']['title'],
                'Selftext': post['data']['selftext'],
                'Upvote_ratio': post['data']['upvote_ratio'],
                'Ups': post['data']['ups'],
                #'Downs': post['data']['downs'],    # Zakomentarisao sam ga jer je nekako uvek 0, a ni ne postoji Downvote_ratio, vrv da se ne bedare ljudi i slicno.. kao sto su ukinuli dislike na YT
                'Author': post['data']['author'],
                'Name': post['data']['name']    # Nema potrebe da se kreira "fullname", ovo je "fullname"
            }, ignore_index=True)

        return df
        
if __name__ == '__main__':
    prom = Ostalo()
    prom1 = prom.nekaFunkcija()
    print(prom1)