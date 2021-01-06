student = input()

grade = 1
bad_grades = 0
average_grade = 0.0
sum_grades = 0.0

while grade <= 12:
    annual_grade = float(input())

    if annual_grade < 4.00:
        bad_grades += 1

        if bad_grades == 2:
            break
        continue
    sum_grades += annual_grade
    average_grade = sum_grades / grade

    grade += 1


if bad_grades == 2:
    print(f'{student} has been excluded at {grade} grade')
else:
    print(f'{student} graduated. Average grade: {average_grade:.2f}')
