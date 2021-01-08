n = int(input())

students = {}

for _ in range(n):
    student = input()
    grade = float(input())
    if student in students:
        students[student].append(grade)
    else:
        students[student] = [grade]

sorted_students = dict(sorted(students.items(), key= lambda x: -sum(x[1]) / len(x[1])))

for student, grade in sorted_students.items():
    if sum(grade) / len(grade) >= 4.50:
        print(f'{student} -> {(sum(grade) / len(grade)):.2f}')



