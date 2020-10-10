import json
import logging
from modules.students_sample import Students
from modules.tutors_sample import Tutors

logging.basicConfig(level=logging.DEBUG,
                    filename="main_py.log",
                    filemode="w")

logging.info("Start program \n")

def run():
    def read_file(file_path):
        """Opening correct json file
        """
        configs = open(file_path)
        return json.loads(configs.read())

    """Student object
    """
    person_data = read_file(file_path='../configs/students_config.json')
    student_1 = Students(person_data)
    logging.info('Student \n')
    logging.info(f'Student name: {student_1.name}')
    logging.info(f'Student surname: {student_1.surname}')
    logging.info(f'Student age: {student_1.get_age()}')
    student_1.set_sex(sex='Female')
    logging.info(f'Student sex: {student_1.sex}')
    logging.info(f'Student average mark: {student_1.avg_mark(person_data)} \n')

    """Tutor object
    """
    person_data = read_file(file_path='../configs/tutors_config.json')
    tutor_1 = Tutors(person_data)
    logging.info('Tutor \n')
    logging.info(f'Tutor name: {tutor_1.name}')
    logging.info(f'Tutor surname: {tutor_1.surname}')
    logging.info(f'Tutor age: {tutor_1.get_age()}')
    tutor_1.set_sex(sex='Male')
    logging.info(f'Tutor sex: {tutor_1.sex}')
    logging.info(f'Tutor experience: {tutor_1.year_exp(person_data)} \n')

    logging.info(f'Namespaces of current program: {dir()} \n')

    logging.info("End program")

if __name__ == "__main__":
    run()
