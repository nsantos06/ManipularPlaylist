#Adicionando as músicas na última playlist criada.*

adicionar_musicas = input('Digite a música e o Artista:')
lista_de_musicas = []

while adicionar_musicas != 'sair':
    resultado = sp.search(q=adicionar_musicas)
    lista_de_musicas.append(resultado['tracks']['items'][0]['uri'])
    adicionar_musicas = input("Digite a música e o Artista:")

prePlaylist = sp.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

sp.playlist_add_items(playlist_id=playlist, items= lista_de_musicas)

#* Caso se a música não existir, ou não estiver disponível no spotify, uma música aleatória será adicionada.
#* Buscar primeiro pelo artista => depois pela música.

