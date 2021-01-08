string_1 = input()
string_2 = input()

current_string = ''
previous_string = string_1

for i in range(len(string_1)):
    for index_2 in range(0, i + 1):
        current_string += string_2[index_2]
    for index_1 in range(ii + 1, len(string_1)):
        current_string += string_1[index_1]
    if not previous_string == current_string:
        print(current_string)
    previous_string = current_string
    current_string = ''






