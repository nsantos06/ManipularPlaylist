import spotipy
from spotipy import SpotifyOAuth
import json

scope = 'playlist-modify-public'
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''

#Criando o Objeto SP.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               scope=scope,
                                               redirect_uri=REDIRECT_URI))

#Pegando ID do usuário.
user_id = sp.me()['id']

#Token de acesso.
token = SpotifyOAuth(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URI,
                     scope=scope,
                     username=user_id)

#Nome e Descrição da Playlist, depois criando-a.
playlist = input("Name:")
description = input("Description:")
sp.user_playlist_create(user=user_id, name=playlist, description=description)

#Nome da música e artista.
track = input("\nTrack:")
artist = input("Artist:")
#lista para guardar as músicas.
list_of_tracks = []

while track != '0':
    #Buscando a musica e o artista.
    searchQuery = track + ' ' + artist
    searchResults = sp.search(q=searchQuery)

    #Achando nome e ID do artista
    searchArtists = searchResults['tracks']['items'][0]['artists']
    searchNameArtist = searchArtists[0]['name']
    searchURIArtist = searchArtists[0]['uri']

    #Achando nome e ID da musica.
    searchNameSong = searchResults["tracks"]["items"][0]["name"]
    searchURISong = searchResults["tracks"]["items"][0]["uri"]
    
    #Imprimindo nome e ID da musica e do Artista.
    print(f'\nArtista:{searchNameArtist}\nURI Artista:{searchURIArtist}')
    print(f'Nome da música:{searchNameSong}\nURI da Musica:{searchURISong}')
    
    #Adicionando URI na lista de sons.
    list_of_tracks.append(searchURISong)

    track = input("\nTrack:")
    artist = input("Artist:")

playlist_user = sp.user_playlists(user=user_id)
playlist_add = playlist_user['items'][0]['id']
sp.playlist_add_items(playlist_id=playlist_add, items=list_of_tracks)
