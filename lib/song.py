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
        # Incrementing the count cls attr
        Song.count += 1
        
        # Appending the genre and artist to cls lists if not included
        if genre not in Song.genres:
            Song.genres.append(genre)
        if artist not in Song.artists:
            Song.artists.append(artist)
        
        # Updating the genre-count dict
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        # Updating the artist-count dict
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @classmethod
    def add_to_genres(cls):
        # Creating a set of unique genres and assigning it to the cls attr
        unique_genres = set(cls.genres)
        cls.genres = list(unique_genres)

    @classmethod
    def add_to_artists(cls):
        # Creating a set of unique artists and assigning it to the cls attr
        unique_artists = set(cls.artists)
        cls.artists = list(unique_artists)

    @classmethod
    def add_to_genre_count(cls):
        # Creating a new genre count dict and updating the cls attr
        genre_count = {}
        for genre in cls.genres:
            genre_count[genre] = cls.genre_count.get(genre, 0)
        cls.genre_count = genre_count

    @classmethod
    def add_to_artist_count(cls):
        # Creating a new artist count dict and updating the cls attr
        artist_count = {}
        for artist in cls.artists:
            artist_count[artist] = cls.artist_count.get(artist, 0)
        cls.artist_count = artist_count