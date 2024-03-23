class Friend:
    def __init__(self, name, film):
        self.name = name
        self.films = [film]

    def display(self):
        pass

    def display_lent_films(self):
        pass


class FriendFilm(Friend):
    def __init__(self, name, film):
        super().__init__(name, film)

    def display(self):
        print(f"-- {self.name} has: ")
        for x in self.films:
            x.display()

    def display_lent_films(self):
        for x in self.films:
            x.display()


class FriendNoFilm(Friend):
    def __init__(self, name, film):
        super().__init__(name, film)

    def display(self):
        print(f"-- {self.name} has no films --")
