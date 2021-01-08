n = int(input())

heroes = {}

for i in range(n):
    hero = input().split()
    hero_name = hero[0]
    hit_points = int(hero[1])
    mana_points = int(hero[2])
    heroes[hero_name] = [hit_points, mana_points]


def cast_spell(heroes, hero_name, mp_needed, spell_name):
    if heroes[hero_name][1] >= mp_needed:
        heroes[hero_name][1] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return heroes[hero_name][1]


def take_damage(heroes, hero_name, damage, attacker):
    heroes[hero_name][0] -= damage
    if heroes[hero_name][0] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
    else:
        heroes.pop(hero_name)
        print(f"{hero_name} has been killed by {attacker}!")
    return heroes


def recharge(heroes, hero_name, amount):
    if heroes[hero_name][1] + amount > 200:
        amount = 200 - heroes[hero_name][1]
        heroes[hero_name][1] = 200
    else:
        heroes[hero_name][1] += amount
    print(f"{hero_name} recharged for {amount} MP!")
    return heroes[hero_name][1]


def heal(heroes, hero_name, amount):
    if heroes[hero_name][0] + amount > 100:
        amount = 100 - heroes[hero_name][0]
        heroes[hero_name][0] = 100
    else:
        heroes[hero_name][0] += amount
    print(f"{hero_name} healed for {amount} HP!")
    return heroes[hero_name][0]


text = input()

while not text == "End":
    command = text.split(' - ')
    if 'CastSpell' in command:
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        cast_spell(heroes, hero_name, mp_needed, spell_name)
    elif 'TakeDamage' in command:
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        take_damage(heroes, hero_name, damage, attacker)
    elif 'Recharge' in command:
        hero_name = command[1]
        amount = int(command[2])
        recharge(heroes, hero_name, amount)
    elif 'Heal' in command:
        hero_name = command[1]
        amount = int(command[2])
        heal(heroes, hero_name, amount)

    text = input()

heroes_sorted = sorted(heroes.items(), key=lambda x: (-x[1][0], x[0]))

for hero, value in heroes_sorted:
    print(f"{hero}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
