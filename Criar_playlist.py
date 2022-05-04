import spotipy
from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOAuth
import requests

scope = 'playlist-modify-public'
username = ''
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''


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
