class Student:
    # Konstruktor może przyjmować wartości
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

# Obiekty możemy przekazywać jako argumenty do funkcji
def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")

# W funkcji możemy zmodyfikować stan obiektu (side effect)
def promote_student(student):
   student.promoted = True

def run_example():
    student = Student(first_name="Alicja", last_name="Jankowska")
    print_student(student)
    promote_student(student)
    print_student(student)

    other_student = Student("Jerzy", "Jurkowski")
    print_student(other_student)

    promote_student(other_student)
    print_student(other_student)

if __name__ == '__main__':
    run_example()