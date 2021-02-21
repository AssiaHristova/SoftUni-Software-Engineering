from collections import deque

bomb_effects = [int(el) for el in input().split(', ')]
bomb_casings = [int(el) for el in input().split(', ')]

bomb_effects_queue = deque(bomb_effects)
bombs = {}
bombs['Datura Bombs'] = 0
bombs['Cherry Bombs'] = 0
bombs['Smoke Decoy Bombs'] = 0

bomb_pouch = False

while bomb_effects_queue:
    if not bomb_casings:
        break
    if bomb_pouch:
        break
    bomb_effect = bomb_effects_queue.popleft()
    bomb_casing = bomb_casings.pop()
    if bomb_effect + bomb_casing == 40:
        bombs['Datura Bombs'] += 1
    elif bomb_effect + bomb_casing == 60:
        bombs['Cherry Bombs'] += 1
    elif bomb_effect + bomb_casing == 120:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        bomb_effects_queue.appendleft(bomb_effect)
        bomb_casing -= 5
        bomb_casings.append(bomb_casing)
    if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
        bomb_pouch = True

if bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects_queue:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(bomb_effect) for bomb_effect in bomb_effects_queue])}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(bomb_casing) for bomb_casing in bomb_casings])}")


sorted_bombs = sorted(bombs.items(), key=lambda x:x[0])
for bomb in sorted_bombs:
    print(f'{bomb[0]}: {bomb[1]}')