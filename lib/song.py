class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
    
        Song.count += 1
    
        if genre not in Song.genres:
            Song.genres.append(genre)
            
        if artist not in Song.artists:
            Song.artists.append(artist)
            
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
@classmethod
def add_to_genres(cls):
    unique_genres = set(Song.genres)
    Song.genres = list(unique_genres)
    
@classmethod
def add_to_artists(cls):
    unique_artists = set(Song.artists)
    Song.artists = list(unique_artists)
    
@classmethod
def add_to_genre_count(cls):
    genre_count = {}
    for song in Song.genre_count:
        if song in genre_count:
           genre_count[song] += 1
        else:
           genre_count[song] = 1
    Song.genre_count = genre_count

@classmethod
def add_to_artist_count(cls):
    artist_count = {}
    for artist in Song.artist_count:
        if artist in artist_count:
           artist_count[artist] += 1
        else:
           artist_count[artist] = 1
    Song.artist_count = artist_count

song = Song("99 Problems", "Jay Z", "Rap")
pass
