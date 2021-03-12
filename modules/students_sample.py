from modules.persons_sample import Persons


class Students(Persons):
    """Student object
        """

    def avg_mark(self, config):
        """Method for getting average mark of a student for current semester
                """
        return sum(config['marks']) / len(config['marks'])

