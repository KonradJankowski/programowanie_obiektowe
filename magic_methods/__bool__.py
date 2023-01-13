import random

class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    def __bool__(self):
        return self.promoted


class School:

    def __init__(self, name, students):
        self.name = name
        self.students = students


def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)
    students = []
    for student_number in range(number_of_students):
        first_name = f"Students-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school

def run_example():
    student = Student(first_name="Konrad", last_name="Jankowski")
    print(bool(student))

    student.promoted = True
    print(bool(student))

    if student:
        print("If student")

    student.promoted = False

    if student:
        print("If student")
    else:
        print("Not promoted")

if __name__ == '__main__':
    run_example()