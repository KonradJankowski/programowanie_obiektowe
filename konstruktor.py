import random


# Obiekt może zawierać w sobie inne obiekty
class School:

    def __init__(self,name ,students):
        self.name = name
        if len(students) > 10:
            students = students[:10]
        self.students = students


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted {student.promoted}")


def promote_student(student):
    student.promoted = True


# Funkcja może zwracać obiekty
def create_school_with_students(school_name, number_of_students):
    # number_of_students = random.randint(1, 20) #losowanie liczby studentów
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}-{school_name}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school

def run_example():
    school = create_school_with_students("Hogwart", 4)
    school_kucykowo = create_school_with_students("Kucykowo", 30)
    print(school)
    print(school_kucykowo)
    for student in school.students:
        print_student(student)
    for student in school_kucykowo.students:
        print_student(student)



if __name__ == '__main__':
    run_example()