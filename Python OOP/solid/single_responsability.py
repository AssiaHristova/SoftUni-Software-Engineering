class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_name(self):
        return self.name


class Formatter:
    def __init__(self, student):
        self.student = student

    def format(self, student):
        return f'Name: {student}'


class Registry:
    def __init__(self):
        self.students = []

    def register(self, student):
        self.students.append(student)

    def unregister(self, student):
        self.students.remove(student)

    def print_registry(self):
        for student in self.students:
            formatter = Formatter(student)
            print(formatter.format(student))


class StudentTaxes:
    def __init__(self, student, semester_tax):
        self.student = student
        self.semester_tax = semester_tax

    def get_student_discount(self):
        return 0


class StudentDiscount(StudentTaxes):
    def get_student_discount(self):
        if self.student.grade >= 5:
            return self.semester_tax * 0.4
        elif self.student.grade >= 4:
            return self.semester_tax * 0.2
        return 0


registry = Registry()
registry.register('Gosho')
registry.print_registry()

st1 = Student('Gosho', 5.50)
st2 = Student('Pesho', 4)
print(StudentDiscount(st1, 100).get_student_discount())
print(StudentDiscount(st2, 100).get_student_discount())

