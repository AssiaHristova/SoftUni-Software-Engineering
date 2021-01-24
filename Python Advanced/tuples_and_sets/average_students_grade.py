n = int(input())

grades = {}

for _ in range(n):
    data = input().split()
    student = data[0]
    grade = float(data[1])
    if student not in grades:
        grades[student] = []
    grades[student].append(grade)

for student, grade in grades.items():
    grades_string = ' '.join(map(lambda x: f'{x:.2f}', grade))
    #grades_string = ' '.join(f'{g:.2f}' for g in grade)
    print(f"{student} -> {grades_string} (avg: {(sum(grade) / len(grade)):.2f})")



