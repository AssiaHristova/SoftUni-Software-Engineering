n = int(input())

positives = []
negatives = []

for i in range(n):
    integer = int(input())
    if integer >= 0:
        positives.append(integer)
    else:
        negatives.append(integer)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")


