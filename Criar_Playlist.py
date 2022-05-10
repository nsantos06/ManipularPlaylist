import spotipy
from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOAuth
import json

scope = 'playlist-modify-public'
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''


#auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                        #client_secret=CLIENT_SECRET)

#Criando o Objeto spotify.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               scope=scope,
                                               redirect_uri=REDIRECT_URI))

#Pegando o ID do usuário
user_id = sp.me()['id']

#Criando o Token de acesso.
token = SpotifyOAuth(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URI,
                     scope=scope,
                     username=user_id)

#Criando a playlist:
nome_playlist = input("Nome da playlist:")
descricao_playlist = input("Descrição da playlist:")

sp.user_playlist_create(user=user_id, name=nome_playlist, description=descricao_playlist)

#Criando a váriavel que pede o nome das músicas
adicionar_musicas = input('Digite a música e o Artista:')
#Criando a lista que guarda as músicas
lista_de_musicas = []

while adicionar_musicas != 'sair':
    resultado = sp.search(q=adicionar_musicas)
    lista_de_musicas.append(resultado['tracks']['items'][0]['uri'])
    adicionar_musicas = input("Digite a música e o Artista:")

prePlaylist = sp.user_playlists(user=user_id)
playlist = prePlaylist['items'][0]['id']

#Adicionando as músicas usando a função playlist_add_items, disponível na biblioteca spotipy.
sp.playlist_add_items(playlist_id=playlist, items= lista_de_musicas)
