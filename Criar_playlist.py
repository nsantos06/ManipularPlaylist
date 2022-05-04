import spotipy
from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOAuth
import requests

scope = 'playlist-modify-public'

username = ''
#A variável username receberá o nome do usuário.
CLIENT_ID = ''
#A variável Client_ID receberá o Client_ID do usuário*.
CLIENT_SECRET = ''
#A variável Client_Secret receberá o Client_Secret do usuário*.
REDIRECT_URI = ''
#A variável Redirect_URI receberá o Redirect_URI do usuário*.

#*As três variáveis, estão disponíveis quando você inicia sua conta como desenvolvedor no Spotify.



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

sp.user_playlist_create('', name=nome_playlist, description=descricao_playlist)

#O primeiro parâmetro, quando usamos o comando user_playlist_create, deverá ser o ID de seu usuário, não o nome.
