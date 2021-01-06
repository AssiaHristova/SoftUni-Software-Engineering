n = int(input())
presentation = input()
sum_all_grades = 0
all_grades = 0

while presentation != 'Finish':
    sum_grades = 0
    avg_grade = 0
    for i in range(1, n + 1):
        grade = float(input())
        sum_grades += grade
        avg_grade = sum_grades / i
        sum_all_grades += grade
        all_grades += 1

    print(f'{presentation} - {avg_grade:.2f}.')

    presentation = input()

print(f"Student's final assessment is {sum_all_grades / all_grades:.2f}.")
