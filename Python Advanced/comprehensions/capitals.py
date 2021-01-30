countries = input().split(', ')
capitals = input().split(', ')

result = zip(countries, capitals)

for ele in result:
    print(f"{ele[0]} -> {ele[1]}")



