line = input().split()
n = int(line[0])
m = int(line[1])

n_nums = set()
m_nums = set()

for _ in range(n):
    n_num = int(input())
    if n_num not in n_nums:
        n_nums.add(n_num)

for _ in range(m):
    m_num = int(input())
    if m_num not in m_nums:
        m_nums.add(m_num)

unique_nums = n_nums.intersection(m_nums)

for num in unique_nums:
    print(num)



