import spotipy
from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOAuth
import requests

scope = 'playlist-modify-public'
username = 'nsantos07'
CLIENT_ID = '6943c8b023dc4b58b9ef14b91be66934'
CLIENT_SECRET = '57dca581357246d795260eaa0413dda3'
REDIRECT_URI = 'http://127.0.0.1:8080/'


token = SpotifyOAuth(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URI,
                     scope=scope,
                     username=username)

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                        client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               scope=scope,
                                               redirect_uri=REDIRECT_URI))
#criando a playlist:
nome_playlist = input("Nome da playlist:")
descricao_playlist = input("Descrição da playlist:")

sp.user_playlist_create('22yw6iqfi6jpql7cyr6tsyjfa', name=nome_playlist, description=descricao_playlist)
