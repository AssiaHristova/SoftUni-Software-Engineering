coins_1_lv = int(input())
coins_2_lv = int(input())
banknotes_5_lv = int(input())
sum_lv = int(input())

for coin_1 in range(coins_1_lv + 1):
    for coin_2 in range(coins_2_lv + 1):
        for banknote in range(banknotes_5_lv + 1):
            if coin_1 + (coin_2 * 2) + (banknote * 5) == sum_lv:
                print(f"{coin_1} * 1 lv. + {coin_2} * 2 lv. + {banknote} * 5 lv. = {sum_lv} lv.")

