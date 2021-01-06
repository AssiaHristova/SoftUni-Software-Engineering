bad_grades = int(input())
problem = input()

average_grade = 0
sum_grades = 0
count = 0
count_bad = 0
grade = 0
last_problem = ''

while problem != 'Enough':
    grade = int(input())
    if grade <= 4:
        count_bad += 1
        if count_bad == bad_grades:
            break
    count += 1
    sum_grades += grade
    average_grade = sum_grades / count
    last_problem = problem

    problem = input()

if count_bad == bad_grades:
    print(f'You need a break, {bad_grades} poor grades.')
else:
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {count}')
    print(f'Last problem: {last_problem}')