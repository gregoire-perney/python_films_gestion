import random


class FilmsLibrary:
    def __init__(self, name, film):
        self.name = name
        self.films = [film]

    def add(self, film):
        self.films.append(film)

    def erase(self):
        self.films.clear()

    def random_film(self):
        print("---------------------------- random_film ------------------------------")
        (random.choice(self.films)).display()
        print("-----------------------------------------------------------------------")

    def display(self):
        print(f"-------------------------- {self.name} ---------------------------")
        for film in self.films:
            film.display()
        print("-----------------------------------------------------------------------")


class FriendsLibrary:
    def __init__(self, name, friend):
        self.name = name
        self.friends = [friend]

    def add(self, film):
        self.friends.append(film)

    def erase(self):
        self.friends.clear()

    def display(self):
        print(f"------------------------- {self.name} --------------------------")
        for friend in self.friends:
            friend.display()
        print("-----------------------------------------------------------------------")

    def display_lent_films(self):
        print("----------------------------- lent_films ------------------------------")
        for friend in self.friends:
            friend.display_lent_films()
        print("-----------------------------------------------------------------------")