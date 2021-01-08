electrons = int(input())

shells = []
n = 1

while electrons > 0:
    max_electrons = 2 * n ** 2
    if (electrons - max_electrons) >= 0:
        shell = max_electrons
        electrons -= shell
        shells.append(shell)
    else:
        shell = electrons
        electrons -= shell
        shells.append(shell)

    n += 1

print(shells)


