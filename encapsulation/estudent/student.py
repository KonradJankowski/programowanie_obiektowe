from estudent.grade import Grade


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self.final_grades = []


    def __str__(self):
        #this is a place where how print info about Student
        return f"Student: {self.first_name} {self.last_name}, promoted: {self.promoted}"

    #method to promote student, defaulted student does not have promoted
    def promote(self):
        self.promoted = True

    # def add_final_grade(self, grade):
    #     self.final_grades.append(grade)
    #     if grade == 1:
    #         self.promoted = False

    def add_final_grade(self, grade):
        self.final_grades.append(Grade(value=grade))
        if grade == 1:
            self.promoted = False

