import spotipy
from spotipy import SpotifyOAuth
import json

scope = 'playlist-modify-public'
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''

# Criando Objeto Spotify(nome sp).
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               scope=scope,
                                               redirect_uri=REDIRECT_URI))
# Pegando o ID do usuário
user_id = sp.me()['id']

# Criando Token de Acesso à conta.
token = SpotifyOAuth(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URI,
                     scope=scope,
                     username=user_id)

def criar_Playlist():
    # Nome e descrição da playlist. Após, ela é criada.
    playlist = input("Name:")
    description = input("Description:")
    sp.user_playlist_create(user=user_id, name=playlist, description=description)

def adicionando_playlist():
    # Pegando as Informações da playlist do usuário.
    playlist_user = sp.user_playlists(user=user_id)
    # Pegando o ID da última playlist. Ou seja, a playlist que foi criada.
    playlist_add = playlist_user['items'][0]['id']
    # Adicionando os itens dentro da lista:
    sp.playlist_add_items(playlist_id=playlist_add, items=list_of_tracks)

def mostrar_playlist():
    playlists = sp.user_playlists(user_id)
    print("\nPlaylists:")
    for playlist in playlists['items']:
        print(playlist['name'])

criar_Playlist()

# Nome do Artista e da música
artist = input("\nArtist:")
track = input("Track:")
# Lista onde as músicas seram guardadas.
list_of_tracks = []
contador_de_musicas = 0

while contador_de_musicas != '0':
    #Só podemos adicionar um limite de 100 músicas na playlist
    contador_de_musicas = contador_de_musicas + 1

    # Fazendo a Busca do artista e da música.
    searchQuery = artist + ' ' + track
    searchResults = sp.search(q=searchQuery)

    # Fazendo a busca do Nome e ID do artista
    searchArtists = searchResults['tracks']['items'][0]['artists']
    searchNameArtist = searchArtists[0]['name']
    searchURIArtist = searchArtists[0]['uri']

    # Encontrando o nome e ID da musica.
    searchNameSong = searchResults["tracks"]["items"][0]["name"]
    searchURISong = searchResults["tracks"]["items"][0]["uri"]

    # print(f'\nArtista:{searchNameArtist}\nURI Artista:{searchURIArtist}')
    # print(f'Nome da música:{searchNameSong}\nURI da Musica:{searchURISong}')

    # Adicionando a Música na lista.
    list_of_tracks.append(searchURISong)
    # Imprimindo a música adicionada e o cantor.
    print(f'\nMúsica {searchNameSong} do(a) {searchNameArtist} Adicionada!')
    print(f'Quantidade de músicas adicionadas:{contador_de_musicas}')

    if contador_de_musicas == 99:
        break

    artist = input("\nArtist:")
    track = input("Track:")

adicionando_playlist()
mostrar_playlist()
