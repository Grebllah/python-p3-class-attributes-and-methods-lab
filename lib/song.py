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
        self.add_song_to_count(name, artist, genre)

    @classmethod
    def add_song_to_count(cls, name, artist, genre, increment=1,):
        cls.count += increment
        if not genre in Song.genres:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1
        else: Song.genre_count[genre] += 1
        if not artist in Song.artists:
            Song.artists.append(artist)
            Song.artist_count[artist] = 1
        else: Song.artist_count[artist] += 1