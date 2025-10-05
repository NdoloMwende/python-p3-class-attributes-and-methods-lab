class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Control for duplicates when you code your add_to_genres class method, 
    # not when you add genres to the original genres list.

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

getYellow = Song("Get Yellow","Jake","Pop")


gotYouRight= Song("Got You Right","Megan Thee Stallion","Hip-Hop")


captainHook = Song("Captain Hook","Megan Thee Stallion","Hip-Hop")


print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)


# class Album:

#     album_count = 0
#     GENRES = ["Hip-Hop", "Pop", "Jazz"]

#     def __init__(self,genre,date):
#         if self.check_genre(genre):
#             self.increase_album_count()
#             self.genre = genre
#             self.release_date = date

#     @classmethod
#     def check_genre(cls,genre):
#         return genre in cls.GENRES
    
#     @classmethod
#     def increase_album_count(cls,increment = 1):
#         cls.album_count += increment

# album = Album(1991)
# skin = Album(2013)
# print(album.release_date)
# print(album.album_count)
# print(Album.album_count)

