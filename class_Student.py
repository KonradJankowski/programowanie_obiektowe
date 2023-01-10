import random


class School:
    
    def __init__(self, name, students):
        self.name = name
        self.students = students
        self.age = None




class Student:

    # Konstruktor może przyjąć argumenty
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self.age = None

    # Obiekty możemy przekazywać jako argumenty do
def print_student(student):
    if student.age != None:
        print(f"Student: {student.first_name} {student.last_name}, age: {student.age}, promoted: {student.promoted}")
    else:
        print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")

def student_set_age(student,age):
    student.age = age

    # side effecr
def promoted_student(student):
    student.promoted = True

def creat_school_with_students(school_name):
    number_of_students = random.randint(1,20)
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name,last_name))

    school = School(school_name, students)
    return school


def run_example():
    student = Student(first_name="Ola", last_name="Nowak")
    print_student(student)
    promoted_student(student)
    print_student(student)

    other_student = Student("Jerzy", "Jurkowski")
    promoted_student(other_student)
    print_student(other_student)

    konrad = Student("Konrad","Jankowski")
    promoted_student(konrad)
    student_set_age(konrad, 18)
    print_student(konrad)

    school = creat_school_with_students("Poko-poko")
    print(school)
    for student in school.students:
        # set random age beetwen 19-35
        x = random.randint(19, 36)
        # set random if student is promoted or not
        if x % 2 == 0:
            promoted_student(student)
        student_set_age(student, x)
        print_student(student)

if __name__ == '__main__':
    run_example()
