from collections import deque

bullet_price = int(input())
bullets_per_barrel = int(input())
bullets = input().split()
locks_sequence = input().split()
intelligence = int(input())

locks = deque()

for el in locks_sequence:
    locks.append(int(el))

bullets = [int(el) for el in bullets]

bullets_in_barrel = bullets_per_barrel

while locks:
    lock = locks[0]
    while bullets:
        bullet = bullets.pop()
        bullets_in_barrel -= 1
        intelligence -= bullet_price
        if bullet <= lock:
            print("Bang!")
        else:
            print("Ping!")

        if bullets_in_barrel == 0:
            if bullets:
                if len(bullets) <= bullets_per_barrel:
                    bullets_in_barrel += len(bullets)
                else:
                    bullets_in_barrel = bullets_per_barrel
                print("Reloading!")

        if bullet <= lock:
            locks.popleft()
            break

    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${intelligence}")
        break

    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break



