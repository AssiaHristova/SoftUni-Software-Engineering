import sys

pairs = int(input())

pair_sum = 0
total_sum = 0
diff = 0
even_pair_sum = 0
odd_pair_sum = 0
max_diff = -sys.maxsize

for pair in range(1, pairs + 1):
    num1 = int(input())
    num2 = int(input())
    pair_sum = num1 + num2
    total_sum += pair_sum
    if pair % 2 == 0:
        even_pair_sum = pair_sum
        if even_pair_sum > odd_pair_sum:
            diff = even_pair_sum - odd_pair_sum
        else:
            diff = odd_pair_sum - even_pair_sum
        if diff > max_diff:
            max_diff = diff
    else:
        odd_pair_sum = pair_sum

if total_sum == pair_sum * pairs:
    print(f"Yes, value={pair_sum}" )
else:
    print(f"No, maxdiff={max_diff}" )


