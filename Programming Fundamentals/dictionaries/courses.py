data = input()

courses = {}

while not data == "end":
    data_list = data.split(" : ")
    course = data_list[0]
    student = data_list[1]
    if course in courses:
        courses[course].append(student)
        sorted_students = sorted(courses[course])
        courses[course] = sorted_students
    else:
        courses[course] = [student]

    data = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))


for course, students in sorted_courses.items():
    print(f"{course}: {len(students)}")
    print(' -- ', end='')
    print('\n -- '.join(students))
