start = int(input())
end = int(input())
magic_n = int(input())
count = 0
is_found = False

for i in range(start, end + 1):
    if is_found:
        break
    for j in range(start, end + 1):
        count += 1
        if i + j == magic_n:
            is_found = True
            print(f'Combination N:{count} ({i} + {j} = {magic_n})')
            break

if not is_found:
    print(f'{count} combinations - neither equals {magic_n}')