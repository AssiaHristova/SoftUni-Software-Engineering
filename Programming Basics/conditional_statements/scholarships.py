import math

income = float(input())
grade = float(input())
minimum_salary = float(input())

social_scholarship = math.floor(minimum_salary * 35/100)
excellent_grade_scholarship = math.floor(grade * 25)

if income < minimum_salary and grade >= 4.5:
    x = social_scholarship
else:
    x = 0

if grade >= 5.5:
    y = excellent_grade_scholarship
else:
    y = 0

if x == 0 and y == 0:
    print('You cannot get a scholarship!')
elif x == social_scholarship and y == 0:
    print(f'You get a Social scholarship {social_scholarship} BGN')
elif x == 0 and y == excellent_grade_scholarship:
    print(f'You get a scholarship for excellent results {excellent_grade_scholarship} BGN')
elif x == social_scholarship and y == excellent_grade_scholarship:
    if social_scholarship > excellent_grade_scholarship:
        print(f'You get a Social scholarship {social_scholarship} BGN')
    else:
        print(f'You get a scholarship for excellent results {excellent_grade_scholarship} BGN')





