students = int(input())

weak_grades = 0
average_grades = 0
good_grades = 0
excellent_grades = 0
avg_grade = 0

for student in range(1, students + 1):
    grade = float(input())
    avg_grade += grade
    if 2 <= grade <= 2.99:
        weak_grades += 1
    elif 3 <= grade <= 3.99:
        average_grades += 1
    elif 4 <= grade <= 4.99:
        good_grades += 1
    elif grade >= 5:
        excellent_grades += 1

print(f"Top students: {(excellent_grades / students) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(good_grades / students) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(average_grades / students) * 100:.2f}%")
print(f"Fail: {(weak_grades / students) * 100:.2f}%")
print(f"Average: {avg_grade / students:.2f}")

