import datetime
from modules.persons_sample import Persons


class Tutors(Persons):
    """Student object
           """

    def year_exp(self, config):
        """Method for getting tutor year experience
                """
        now = datetime.datetime.now()
        current_year = now.year
        return current_year - config['tutor_start']
