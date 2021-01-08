command = input()

companies = {}

while not command == "End":
    command_list = command.split(' -> ')
    company = command_list[0]
    employee_id = command_list[1]
    if company in companies:
        if employee_id not in companies[company]:
            companies[company].append(employee_id)
    else:
        companies[company] = [employee_id]

    command = input()

sorted_companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for company, employee_id in sorted_companies.items():
    print(f'{company}')
    print('-- ', end='')
    print('\n-- '.join(employee_id))
