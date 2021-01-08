employees_happiness = input().split()
happiness_improvement_factor = int(input())

increased_happiness = [int(num) * happiness_improvement_factor for num in employees_happiness]
average_happiness = sum(increased_happiness) / len(increased_happiness)
greater_than_average_happiness = [num for num in increased_happiness if num >= average_happiness]

if len(greater_than_average_happiness) * 2 >= len(increased_happiness):
    print(f"Score: {len(greater_than_average_happiness)}/{len(increased_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(greater_than_average_happiness)}/{len(increased_happiness)}. Employees are not happy!")