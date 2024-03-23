class Film:
    def __init__(self, name, creation_date):
        self.name = name
        self.creation_date = creation_date

    def display(self):
        pass


class FilmUF(Film):
    def __init__(self, name, creation_date):
        super().__init__(name, creation_date)

    def display(self):
        print(f"-- {self.name}, published in {self.creation_date}, unknown format --")


class FilmVHF(Film):
    def __init__(self, name, creation_date, kind):
        super().__init__(name, creation_date )
        self.kind = kind

    def display(self):
        print(f"-- {self.name}, published in {self.creation_date}, {self.kind} format --")


class FilmDVD(Film):
    def __init__(self, name, creation_date, kind):
        super().__init__(name, creation_date)
        self.kind = kind

    def display(self):
        print(f"-- {self.name}, published in {self.creation_date}, {self.kind} format --")