class TooManyStudents(Exception): 
    pass

class Classroom:
    MAX_STUDENTS = 10

    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title

    def add_student(self, student):
        if len(self.students) < self.MAX_STUDENTS:
            self.students.append(student)
        else:
            raise TooManyStudents("Cannot add more students, limit reached ({self.MAX_STUDENTS}).")
        
    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break

    def change_teacher(self, new_teacher):
        self.teacher = new_teacher

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

class Student(Person):
    pass