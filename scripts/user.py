from scripts import database as db, cleaning as c, films as fi, library as lb, friends as fr


class User:
    def create_films_library(self, library):
        film = fi.Film(name=None, creation_date=None)
        return lb.FilmsLibrary(name=library, film=film)

    def add_films(self, library):
        def getkey(element):
            return element[0]
        for film in sorted(c.CleaningTool(db.films).clean_films(), key=getkey):
            if 'vhf' in film:
                film = fi.FilmVHF(name=film[0], creation_date=film[1], kind='vhf')
            elif 'dvd' in film:
                film = fi.FilmDVD(name=film[0], creation_date=film[1], kind='dvd')
            else:
                film = fi.FilmUF(name=film[0], creation_date=film[1])
            library.add(film)
        return library

    def sort_films_name(self, library):
        library.erase()

        def getkey(element):
            return element[0]
        for film in sorted(c.CleaningTool(db.films).clean_films(), key=getkey):
            if 'vhf' in film:
                film = fi.FilmVHF(name=film[0], creation_date=film[1], kind='vhf')
            elif 'dvd' in film:
                film = fi.FilmDVD(name=film[0], creation_date=film[1], kind='dvd')
            else:
                film = fi.FilmUF(name=film[0], creation_date=film[1])
            library.add(film)
        return library

    def sort_films_date(self, library):
        library.erase()

        def getkey(element):
            return element[1]
        for film in sorted(c.CleaningTool(db.films).clean_films(), key=getkey):
            if 'vhf' in film:
                film = fi.FilmVHF(name=film[0], creation_date=film[1], kind='vhf')
            elif 'dvd' in film:
                film = fi.FilmDVD(name=film[0], creation_date=film[1], kind='dvd')
            else:
                film = fi.FilmUF(name=film[0], creation_date=film[1])
            library.add(film)
        return library

    def sort_films_format(self, library):
        library.erase()

        def getkey(element):
            return element[2]
        for film in sorted(c.CleaningTool(db.films).clean_films(), key=getkey):
            if 'vhf' in film:
                film = fi.FilmVHF(name=film[0], creation_date=film[1], kind='vhf')
            elif 'dvd' in film:
                film = fi.FilmDVD(name=film[0], creation_date=film[1], kind='dvd')
            else:
                film = fi.FilmUF(name=film[0], creation_date=film[1])
            library.add(film)
        return library

    def create_friends_library(self, library):
        friend = fr.Friend(name=None, film=None)
        return lb.FriendsLibrary(name=library, friend=friend)

    def add_friends(self, friends_library, films_library):
        def getkey(element):
            return element[0]

        for friend in sorted(c.CleaningTool(db.friends).clean_friends(), key=getkey):
            if len(friend) == 2:
                film_name = friend[1]
                for x in films_library.films:
                    if x.name == film_name:
                        friend = fr.FriendFilm(name=friend[0], film=x)
            else:
                friend = fr.FriendNoFilm(name=friend[0], film=None)
            friends_library.add(friend)
        return friends_library
