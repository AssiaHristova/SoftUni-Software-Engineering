sequence = input().split()
command = input()

shot = 0
targets = [int(target) for target in sequence]

while not command == "End":
    index = int(command)
    if index in range(0, len(targets)):
        for i in range(len(targets)):
            if not i == index:
                if targets[i] >= 0:
                    if targets[i] > targets[index]:
                        targets[i] -= targets[index]
                    else:
                        targets[i] += targets[index]
        targets[index] = - 1
        shot += 1

    command = input()

targets_str = [str(target) for target in targets]

if command == "End":
    print(f"Shot targets: {shot} -> {' '.join(targets_str)}")

