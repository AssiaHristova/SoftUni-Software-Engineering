import re
participants = input().split(", ")
line = input()

pattern_name = r'[a-zA-Z]'
pattern_distance = r'[0-9]'

racers = {}

while not line == "end of race":
    letters = re.findall(pattern_name, line)
    name = ''.join(letters)
    digits = re.findall(pattern_distance, line)
    digits = [int(digit) for digit in digits]
    distance = sum(digits)
    if name in participants:
        if name in racers:
            racers[name] += distance
        else:
            racers[name] = distance

    line = input()

sorted_racers = sorted(racers.items(),key=lambda x:-x[1])
winning_racers = sorted_racers[:3]
print(f"1st place: {winning_racers[0][0]}")
print(f'2nd place: {winning_racers[1][0]}')
print(f'3rd place: {winning_racers[2][0]}')