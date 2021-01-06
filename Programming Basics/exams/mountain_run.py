import math

record = float(input())
distance = float(input())
speed = float(input())

time = distance * speed
slowdown = (math.floor(distance / 50)) * 30
final_time = time + slowdown
sec_out = final_time - record

if final_time < record:
    print(f"Yes! The new record is {final_time:.2f} seconds.")
else:
    print(f"No! He was {sec_out:.2f} seconds slower.")


