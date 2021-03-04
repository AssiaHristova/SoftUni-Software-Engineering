def generate_line(count, symbol, offset_count=0):
    offset = offset_count * ' '
    asterixes = (f'{symbol} ' * count).strip()
    return f'{offset}{asterixes}'


def draw_line(count, symbol, offset_count=0):
    print(generate_line(count, symbol, offset_count))


def draw_rhombus(n):
    for i in range(n):
        draw_line(i + 1, '*', n - i - 1)

    for i in range(n - 2,  - 1, -1):
        draw_line(i + 1, '*', n - i - 1)


def draw_triangle(n):
    for i in range(n):
        draw_line(i + 1, '+')

    for i in range(n - 2,  - 1, -1):
        draw_line(i + 1, '+')


draw_rhombus(1)
draw_rhombus(2)
draw_rhombus(3)
draw_rhombus(4)
draw_triangle(3)

