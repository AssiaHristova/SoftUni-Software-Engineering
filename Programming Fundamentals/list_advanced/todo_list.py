note = input()

todo_list = [0 for _ in range(11)]

while not note == 'End':
    note_list = note.split('-')
    importance = int(note_list[0])
    task = note_list[1]
    todo_list.insert(importance, task)

    note = input()

result = [task for task in todo_list if not task == 0]
print(result)
