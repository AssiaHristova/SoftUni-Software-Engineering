nums = [int(el) for el in input().split()]

positives = [num for num in nums if num >= 0]
negatives = [num for num in nums if num < 0]

sum_positives = sum(positives)
sum_negatives = sum(negatives)

print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
