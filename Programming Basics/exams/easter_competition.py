import sys
breads = int(input())

max_grade = -sys.maxsize
max_baker = ''

for bread in range(1, breads + 1):
    baker_name = input()
    grades_per_baker = 0
    command = input()
    while command != 'Stop':
        grade = int(command)
        grades_per_baker += grade
        if grades_per_baker > max_grade:
            max_grade = grades_per_baker
            max_baker = baker_name

        command = input()

    if command == 'Stop':
        print(f"{baker_name} has {grades_per_baker} points.")
        if max_grade == grades_per_baker:
            print(f"{baker_name} is the new number 1!")


print(f"{max_baker} won competition with {max_grade} points!")



