import datetime


class Persons():
    """Person object
    """

    def __init__(self, config):
        """Person properties
        """

        self.name = config['name']
        self.surname = config['surname']
        self.birth_year = config['birth_year']
        self.sex = None

    def get_age(self):
        """Method for getting age by provided birth year"""
        now = datetime.datetime.now()
        current_year = now.year
        return current_year - self.birth_year

    def set_sex(self, sex):
        """Method for adding sex of a person"""
        self.sex = sex
        return sex

