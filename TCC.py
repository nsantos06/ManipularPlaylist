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


#Criando Token de Acesso à conta.
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
    account_name = sp.me()['display_name']
    print(f'Nome das playlists na conta do(a) {account_name}:\n')
    for playlist in playlists['items']:
        print(playlist['name'])

criar_Playlist()

quantity_tracks = int(input("Quantas músicas deseja adicionar?: "))
#Quando o usuário pedir pra adicionar um número de músicas inválidas.
while quantity_tracks < 1:
    print("Digite um número de 1 até 100")
    quantity_tracks = int(input("Quantas músicas deseja adicionar?: "))
#Dado o limite de até 100 faixas por execução de código, o usuário poderá colocar até 99.
while quantity_tracks >= 100:
    print("Digite um numero menor que 100")
    quantity_tracks = int(input("Quantas musicas deseja adicionar?:"))


# Nome do Artista e da música
artist = input("\nArtista:")
track = input("Faixa musical:")

# Lista onde as músicas seram guardadas.
list_of_tracks = []

#Contador de faixas
count_tracks = 0

while track != '0':
    #Só podemos adicionar um limite de 100 músicas na playlist
    count_tracks = count_tracks + 1

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
    print(f'\nUma música similar à: {searchNameSong} do(a) {searchNameArtist} foi adicionada!')
    print(f'Quantidade de músicas adicionadas:{count_tracks}')

    #O programa parará quando a contagem de faixas for igual a quantidade, ou chegar no limite(100).

    if count_tracks == quantity_tracks or count_tracks == 100:
        break

    artist = input("\nArtista:")
    track = input("Faixa musical:")

adicionando_playlist()
mostrar_playlist()
