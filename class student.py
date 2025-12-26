class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    def display(self):
        print("Student Details")
        print("----------------")
        print("Roll No:", self.roll_no)
        print("Name   :", self.name)
        print("Marks  :", self.marks)
    def result(self):
        if self.marks >= 40:
            print("Result : Pass")
        else:
            print("Result : Fail")
