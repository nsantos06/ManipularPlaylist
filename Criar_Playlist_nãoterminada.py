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

#Pedindo o nome do artista.
artista = input("Digite o nome do artista:")

#Pedindo o nome da musica.
adicionar_musicas = input('Digite a música:')
#Lista onde as músicas ficaram armazenadas.
lista_de_musicas = []

while adicionar_musicas != 'sair' and artista != 'sair':
    #Procurando o ID do artista.
    resultado = sp.search(artista, 1,0, 'artist')
    artista_nome = resultado['artists']['items'][0]
    artista = artista_nome['uri']

    #Procurando o ID da música.
    procurar_musica = sp.search(q=adicionar_musicas)
    #Adicionando as músicas na lista:
    lista_de_musicas.append(procurar_musica['tracks']['items'][0]['uri'])

    artista = input("Digite o artista:")
    adicionar_musicas = input("Digite a música:")

prePlaylist = sp.user_playlists(user=user_id)
playlist = prePlaylist['items'][0]['id']

sp.playlist_add_items(playlist_id=playlist, items= lista_de_musicas)

