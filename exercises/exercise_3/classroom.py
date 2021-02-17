class Person:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
        
    def print_full_name(self):
        print(f'{self.firstname} {self.lastname}', end = '')
        
class Student(Person):
    def __init__(self, first_name, last_name, subject):
        Person.__init__(self, first_name, last_name)
        self.subject = subject

    def print_name_subject(self):
        self.print_full_name()
        print(f', {self.subject}')
        
class Teacher(Person):
    def __init__(self, first_name, last_name, course_name):
        super(Teacher, self).__init__(first_name, last_name)
        self.coursename = course_name
        
    def print_name_course(self):
        self.print_full_name()
        print(f', {self.coursename}')