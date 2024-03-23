import re


class CleaningTool:
    def __init__(self, listname):
        self.listname = listname

    def clean_films(self):
        list_strings = [''.join(i) for i in self.listname]
        list_strings_lowercase = [x.lower() for x in list_strings]
        list_strings_lowercase_date = [re.sub(r'[()]', ', ', film) for film in list_strings_lowercase]
        list_strings_lowercase_date2 = [re.sub(r'(\s,)', lambda x: x.group().strip(), film) for film in
                                        list_strings_lowercase_date]
        list_strings_lowercase_date2_tuple = [tuple(film.split(', ')) for film in list_strings_lowercase_date2]
        return list_strings_lowercase_date2_tuple

    def clean_friends(self):
        list_strings = [', '.join(i) for i in self.listname]
        list_strings_lowercase = [x.lower() for x in list_strings]
        list_strings_lowercase_tuple = [tuple(film.split(', ')) for film in list_strings_lowercase]
        return list_strings_lowercase_tuple
