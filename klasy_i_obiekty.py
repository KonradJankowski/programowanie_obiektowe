class Student:
    pass


class Grade:
    pass


class School:
    pass

if __name__ == '__main__':


    student_konrad = Student()      #Stworzenie instancji obiektu !!!

    grade_a = Grade()
    grade_f = Grade()

    my_school = School()

    # print(student_konrad)
    # print(grade_a, grade_f)
    # print(my_school)

    print("type(student_konrad):", type(student_konrad))    # stworzyłem typy definjujące classy, matrycę do tworzenia
    print("type(grade_a): ", type(grade_a))                 # kolejnych obiektów
    print("type(grade_f): ", type(grade_f))
    print("type(my_school): ", type(my_school))

    all_students = [Student(), Student(), Student(), Student()]
    print(all_students)
    print(all_students[0])

    grades = {
        1: Grade(),
        2: Grade(),
        3: Grade(),
        4: Grade(),
        5: Grade(),
        6: Grade(),
    }
    print(grades)