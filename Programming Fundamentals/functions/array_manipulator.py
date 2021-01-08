array_given = input().split()
command_given = input().split()


def exchange(array, command):
    array_list = [int(num) for num in array]
    index = int(command[1])
    array_1 = array_list[:index + 1]
    array_2 = array_list[index + 1:]
    if index < len(command):
        array_list = array_2 + array_1
    else:
        print("Invalid index")
    return array_list


def max_min_odd_even(array, command):
    array_list = exchange(array, command='exchange')
    even_list = []
    odd_list = []
    result = 0
    for num in array_list:
        if int(num) % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    if 'max' in command:
        if 'odd' in command:
            if len(odd_list) == 0:
                print("No matches")
            else:
                max_odd = max(odd_list)
                result = odd_list.index(max_odd)
        else:
            if len(even_list) == 0:
                print("No matches")
                max_even = max(even_list)
                result = even_list.index(max_even)
    elif 'min' in command:
        if 'odd' in command:
            if len(odd_list) == 0:
                print("No matches")
            else:
                min_odd = min(odd_list)
                result = odd_list.index(min_odd)
        else:
            if len(even_list) == 0:
                print("No matches")
            else:
                min_even = min(even_list)
                result = even_list.index(min_even)
    return result


def first_last_odd_even(array, command):
    array_list = exchange(array, command)
    even_list = []
    odd_list = []
    result_2 = []
    count = int(command[1])
    for num in array_list:
        if int(num) % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    if 'first' in command:
         if count > len(command):
             print("Invalid count")
         else:
             if 'odd' in command:
                 if count > len(odd_list):
                     result_2 = odd_list
                 else:
                     result_2 = odd_list[:count]
             else:
                 if count > len(even_list):
                     result_2 = even_list
                 else:
                     result_2 = even_list[:count]
    elif 'last' in command:
        if count > len(command):
                print("Invalid count")
        else:
            if 'odd' in command:
                if count > len(odd_list):
                    result_2 = odd_list
                else:
                    result_2 = odd_list[count:]
            else:
                if count > len(even_list):
                    result_2 = even_list
                else:
                    result_2 = even_list[count:]
    return result_2


def array_manipulator(array, command):
    while not command == "end":
        if 'exchange' in command:
            array_list = exchange(array, command='exchange')
        elif 'max' in command:
            result = max_min_odd_even(array, command)
            print(result)
        elif 'first' in command:
            result = first_last_odd_even(array, command)
            print(result)
        command = input()


array_manipulator(array_given, command_given)


