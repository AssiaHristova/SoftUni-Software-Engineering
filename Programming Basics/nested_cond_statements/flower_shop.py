chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

bucket_price = 0

if holiday == 'Y':
    if season == 'Spring':
        if tulips <= 7:
            bucket_price = (chrysanthemums * 2 + roses * 4.10 + tulips * 2.50) * 1.15
        else:
            bucket_price = ((chrysanthemums * 2 + roses * 4.10 + tulips * 2.50) * 1.15 ) * 0.95
        if (chrysanthemums + roses + tulips) > 20:
            bucket_price = bucket_price * 0.8
    elif season == 'Summer':
        bucket_price = (chrysanthemums * 2 + roses * 4.10 + tulips * 2.50) * 1.15
        if (chrysanthemums + roses + tulips) > 20:
            bucket_price = bucket_price * 0.8
    elif season == 'Autumn':
        bucket_price = (chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15) * 1.15
        if (chrysanthemums + roses + tulips) > 20:
            bucket_price = bucket_price * 0.8
    elif season == 'Winter':
        if roses < 10:
            bucket_price = (chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15) * 1.15
        else:
            bucket_price = ((chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15) * 1.15) * 0.9
        if (chrysanthemums + roses + tulips) > 20:
            bucket_price = bucket_price * 0.8
else:
    if season == 'Spring':
        if tulips <= 7:
            bucket_price = chrysanthemums * 2 + roses * 4.10 + tulips * 2.50
        else:
            bucket_price = (chrysanthemums * 2 + roses * 4.10 + tulips * 2.50) * 0.95
        if (chrysanthemums + roses + tulips) > 20:
            bucket_price = bucket_price * 0.8
    elif season == 'Summer':
        bucket_price = chrysanthemums * 2 + roses * 4.10 + tulips * 2.50
        if (chrysanthemums + roses + tulips) > 20:
            bucket_price = bucket_price * 0.8
    elif season == 'Autumn':
        bucket_price = chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15
        if (chrysanthemums + roses + tulips) > 20:
            bucket_price = bucket_price * 0.8
    elif season == 'Winter':
        if roses < 10:
            bucket_price = chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15
        else:
            bucket_price = (chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15) * 0.9
        if (chrysanthemums + roses + tulips) > 20:
            bucket_price = bucket_price * 0.8


print(f'{bucket_price + 2:.2f}')

