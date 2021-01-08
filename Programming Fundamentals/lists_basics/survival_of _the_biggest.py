string = input()
n = int(input())

my_list = string.split(' ')
my_num_list = []

for j in my_list:
    k = int(j)
    my_num_list.append(k)

for i in range(n):
    smallest = min(my_num_list)
    my_num_list.remove(smallest)

print(my_num_list)



