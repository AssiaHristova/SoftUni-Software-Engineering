actor = input()
points_academy = float(input())
n = int(input())

points = 0
total_points = points_academy

for i in range(1, n + 1):
    evaluator = input()
    points_evaluator = float(input())
    points = len(evaluator) * points_evaluator / 2
    total_points += points
    if total_points > 1250.50:
        break

if total_points > 1250.50:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {(1250.5 - total_points):.1f} more!")

