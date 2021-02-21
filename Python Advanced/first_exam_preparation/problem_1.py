from collections import deque

fireworks_effect = [int(el) for el in input().split(', ')]
explosive_power = [int(el) for el in input().split(', ')]

effects = deque(fireworks_effect)
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

firework_show = False


while effects:
    if not explosive_power:
        break
    effect = effects.popleft()
    power = explosive_power.pop()

    while not effect > 0:
        if not effects:
            break
        else:
            effect = effects.popleft()
    if effect <= 0:
        explosive_power.append(power)
        break

    while not power > 0:
        if not explosive_power:
            break
        else:
            power = explosive_power.pop()
    if power <= 0:
        effects.appendleft(effect)
        break

    sum_effects = effect + power
    if sum_effects % 3 == 0 and sum_effects % 5 != 0:
        palm_fireworks += 1
    elif sum_effects % 5 == 0 and sum_effects % 3 != 0:
        willow_fireworks += 1
    elif sum_effects % 5 == 0 and sum_effects % 3 == 0:
        crossette_fireworks += 1
    else:
        effect -= 1
        effects.append(effect)
        explosive_power.append(power)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        firework_show = True
        break

if firework_show:
    print('Congrats! You made the perfect firework show!')
else:
    print('Sorry. You can’t make the perfect firework show.')

if effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in effects])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
