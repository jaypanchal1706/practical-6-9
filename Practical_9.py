"""
    Name = Panchal Jay Manojkumar
    Id = 20CE068

    Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result.
    The Student class has data members such as those representing rollNumber, Name, etc.
    Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects.
    Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship.

    Github Link = https://github.com/jaypanchal1706/practical-6-7.git

"""
class Student:
    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name = name

    def display(self):
        print(f'Student Roll No: {self.rollNo}')
        print(f'Student Name: {self.name}')

class Exam(Student):
    def __init__(self, rollNo, name, subject):
        super().__init__(rollNo, name)
        self.subject = subject

    def display(self):
        super().display()
        for i in range(len(self.subject)):
            print(f'Subject {i} Marks: {self.subject[i]}')


class Result(Exam):
    total_marks = 0

    def __init__(self, rollNo, name, subject):
        super().__init__(rollNo, name, subject)
        self.total_marks = sum(subject)

    def display(self):
        super().display()
        print(f'Total Marks: {self.total_marks}')


if __name__ == '__main__':
    student = Student(53, 'Smit')
    student.display()
    print()

    exam = Exam(51, 'Kirtan', [78, 89, 34])
    exam.display()
    print()

    result = Result(47, 'Brijesh', [90, 98, 93])    
    result.display()
    print()

    result = Result(69, 'Praik', [83, 88, 73])
    result.display()
    print()
