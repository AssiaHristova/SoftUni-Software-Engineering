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

