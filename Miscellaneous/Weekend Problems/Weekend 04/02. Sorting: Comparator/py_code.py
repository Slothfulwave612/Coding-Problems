from functools import cmp_to_key

class Student:
    '''
    a student class.
    '''

    def __init__(self, name, marks):
        '''
        Function to initialize the Student class object.

        Arguments:
        name -- str, the name of the student.
        marks -- int, the marks scored by the student.
        '''
        self.name = name
        self.marks = marks

    def comparator(a, b):
        if a.marks < b.marks:
            return 1
        if a.marks > b.marks:
            return -1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0

data = [Student('amy', 100), Student('david', 100), Student('heraldo', 50), Student('aakansha', 75), Student('aleksa', 150)]

data = sorted(data, key=cmp_to_key(Student.comparator))

for i in data:
    print(i.name, i.marks)
