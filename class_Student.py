
class Student:

    # Konstruktor może przyjąć argumenty
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

    # Obiekty możemy przekazywać jako argumenty do
    def print_student(student):
        print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")

