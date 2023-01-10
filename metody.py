class Student:

    def __init__(self, name):
        self.name = name

    def print_something(self):
        print("To ja - metoda studenta")

if __name__ == '__main__':
    student = Student(name="Konrad")
    # Wywoływanie metody
    student.print_something()
    print(__name__)