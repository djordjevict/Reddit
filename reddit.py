CLIENT_ID='o6LqV4RYbHv8rnkMazt01g'
SECRET_TOKEN='HWcRqlhlss5bz0I1Z3VJ1t2chg2p0Q'

import requests
import pandas as pd

class RedditAuth():

    def authenticate(self):
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)
        data = {'grant_type': 'password',
        'username': 'Living-Aioli1805',
        'password': 'volimsebe'}
        headers = {'User-Agent': 'OurAPI/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
        TOKEN = res.json()['access_token']
        headers['Authorization'] = f'bearer {TOKEN}'
        return headers

class Ostalo():

    def __init__(self):
        self.headers = RedditAuth().authenticate()

    def nekaFunkcija(self):
        res = requests.get('https//oauth.reddit.com/r/python/hot', headers=self.headers, params={'limit':'10'})

        df = pd.DataFrame()

        for post in res.json()['data']['children']:
            df = df.append({
                'title':post['data']['title']
            }, ignore_index=True)

        return df
        
if __name__ == '__main__':
    prom = Ostalo()
    prom1 = prom.nekaFunkcija()
    print(prom1)