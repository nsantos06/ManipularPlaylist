import spotipy
from spotipy import SpotifyOAuth
import json

scope = 'playlist-modify-public'
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               scope=scope,
                                               redirect_uri=REDIRECT_URI))
user_id = sp.me()['id']
token = SpotifyOAuth(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     redirect_uri=REDIRECT_URI,
                     scope=scope,
                     username=user_id)

track = input("Track:")
artist = input("Artist:")

while track != '0':
    searchQuery = track + ' ' + artist
    searchResults = sp.search(q=searchQuery)

    #Achando nome do artista
    searchArtistname =searchResults['tracks']['items'][0]['artists']
    searchnewArtistname = searchArtistname[0]['name']
    searchArtisturi = searchArtistname[0]['uri']

    print(f'\nArtista:{searchnewArtistname}\nID Artista:{searchArtisturi}')
    #Achando nome da musica e id da musica.
    print(f'Nome da música:{searchResults["tracks"]["items"][0]["name"]}\n'
          f'ID música:{searchResults["tracks"]["items"][0]["uri"]}')

    track = input("\nTrack:")
    artist = input("Artist:")
