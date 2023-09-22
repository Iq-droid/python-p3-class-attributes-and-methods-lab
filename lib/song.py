class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
    #incrementing the count cls attr
        Song.count += 1
    
    #appending the genre and artist to cls if not included
        if genre not in Song.genres:
            Song.genres.append(genre)
            
        if artist not in Song.artists:
            Song.artists.append(artist)
            
    #updating genre-count dict
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
            
    #updating artist-count dict
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
        
@classmethod
def add_to_genres(cls):
    #creating a set of unique genres && assgn it to clas attr
    unique_genres = set(cls.genres)
    cls.genres = list(unique_genres)
    
@classmethod
def add_to_artists(cls):
    #creating a set of unique artists && assgn it to cls attr
    unique_artists = set(cls.artists)
    cls.artists = list(unique_artists)
    
@classmethod
def add_to_genre_count(cls):
    genre_count = {}
    for song in cls.genre_count:
        genre_count[song] = cls.genre_count[song]
    cls.genre_count = genre_count#update the genre-count dict val(nw)

@classmethod
def add_to_artist_count(cls):
    artist_count = {}
    for artist in cls.artist_count:
        artist_count[artist] = cls.artist_count[artist]
    cls.artist_count = artist_count#update artist-count dict val(nw)
    
#creating song obj
song = Song("99 Problems", "Jay Z", "Rap")
pass
