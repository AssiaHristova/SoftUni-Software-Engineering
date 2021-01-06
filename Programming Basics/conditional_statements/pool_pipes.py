V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

V1 = P1 * H
V2 = P2 * H

if V >= V1 + V2:
    print(f'The pool is {((V1 + V2) / V) * 100:.2f}% full. Pipe 1: {(V1 / (V1 + V2)) * 100:.2f}%. Pipe 2: {(V2 / (V1 + V2)) * 100:.2f}%."')
else:
    print(f'For {H} hours the pool overflows with {(V1 + V2) - V:.2f} liters.')
