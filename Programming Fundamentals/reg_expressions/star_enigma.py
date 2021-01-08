import re

n = int(input())

attacked_planets = []
destroyed_planets = []

key_pattern = r'[star]'
planet_pattern = r'@(?P<planet>[a-zA-Z]+)([^@!:>\-]+)?:(?P<population>[0-9]+)([^@!:>\-]+)?!(?P<attack_type>[AD])!([^@!:>\-]+)?->(?P<soldier_count>[0-9]+)'

for _ in range(n):
    line = input()
    message = ''
    key_letters = re.findall(key_pattern, line, re.IGNORECASE)
    key = len(key_letters)
    for letter in line:
        new_letter = chr(ord(letter) - key)
        message += new_letter
    planets = re.finditer(planet_pattern, message)
    for planet in planets:
        p = planet.groupdict()
        planet_name = p['planet']
        population = p['population']
        soldier_count = p['soldier_count']
        attack_type = p['attack_type']
        if attack_type == 'A':
            attacked_planets.append(planet_name)
            attacked_planets.sort()
        else:
            destroyed_planets.append(planet_name)
            destroyed_planets.sort()


print(f"Attacked planets: {len(attacked_planets)}")
for ele in attacked_planets:
    print(f"-> {ele}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for el in destroyed_planets:
    print(f"-> {el}")



