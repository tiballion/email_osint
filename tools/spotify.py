import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_client():
    with open('../config.json') as f:
        config = json.load(f)
    client_id = config['spotify']['client_id']
    client_secret = config['spotify']['client_secret']
    return SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

def spotify(email):
    client = get_client()
    sp = spotipy.Spotify(client_credentials_manager=client)
    results = sp.search(q='email:'+email, type='user')
    if results['users']['total'] > 0:
        return "Spotify \U0001f440"
    else:
        return "Spotify \U0001F6AB"

spotify('dimitrimakarov33+1@gmail.com')