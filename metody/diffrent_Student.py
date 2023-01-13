
class Student:

    def __init__(self, name):
        self.name = name

    def print_something(self):
        print("To ja - metoda studenta!")

    def print_self(self):
        print("Czym jest self?: ", self)
        print("Jest tutaj dostęp do name: ",self.name)

    def do_all_work(self):
        print("Teraz to ja pracuję...")
        self.do_piece_of_work()
        self.do_piece_of_work()
        self.do_piece_of_work()
        print("Koniec:)")

    def do_piece_of_work(self):
        print("Robota...")


if __name__ == '__main__':

    student = Student(name="Konrad")
    #wywołanie metody
    student.print_something()

    # Pierwszy przeazany niejawnie argument, zawiera referencję na aktualny obiekt
    student.print_self()

    # Metoda może wołać inną metodę
    student.do_all_work()

