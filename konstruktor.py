class Student:
    # Konstruktor zostanie wywołąny podczas tworzenia obiektu
    def __init__(self):
        self.first_name = "Konrad"
        self.last_name = "Jankowski"
        self.age = 18

def example():
    student = Student()
    # Do stanu obiektu mamy dostęp - możmy go odczytać
    print(student.first_name)
    print(student.last_name)
    print(student.age)

def second_example():
    student = Student()
    student.first_name = "Aleksander"
    student.age = 12
    print(student.first_name)
    print(student.last_name)
    print(student.age)


if __name__ == '__main__':
    example()
    second_example()