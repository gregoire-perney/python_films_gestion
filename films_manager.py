from scripts import user as u


def main():
    me = u.User()
    library_films = me.create_films_library(library='my_films_library')
    library_friends = me.create_friends_library(library='my_friends_library')

    me.add_films(library_films)
    library_films.display()
    me.sort_films_date(library_films)
    library_films.display()
    me.sort_films_format(library_films)
    library_films.display()
    library_films.random_film()

    me.add_friends(library_friends, library_films)
    library_friends.display()
    library_friends.display_lent_films()


if __name__ == "__main__":
    main()
