breads = int(input())
egg_packs = int(input())
sweets = int(input())


eggs = egg_packs * 12
price = breads * 3.20 + egg_packs * 4.35 + sweets * 5.40 + eggs * 0.15

print(f'{price:.2f}')