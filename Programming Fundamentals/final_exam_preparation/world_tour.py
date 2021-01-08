def add_stop(stops, index, string):
    result = ''
    if index in range(len(stops)):
        result = stops[:index] + string + stops[index:]
        print(result)
        return result
    return stops


def remove_stop(stops, start_i, end_i):
    result = ''
    if start_i in range(len(stops)) and end_i in range(len(stops)):
        result = stops[:start_i] + stops[end_i + 1:]
        print(result)
        return result
    return stops


def switch(stops, old_string, new_string):
    result = ''
    if old_string in stops:
        result = stops.replace(old_string, new_string)
        print(result)
        return result
    return stops


stops = input()
line = input()

while not line == "Travel":
    command = line.split(':')
    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        stops = add_stop(stops, index, string)
    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        stops = switch(stops, old_string, new_string)

    line = input()

print(f"Ready for world tour! Planned stops: {stops}")
