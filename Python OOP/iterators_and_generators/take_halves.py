def solution():
    def integers():
        start_num = 1
        while True:
            integer = start_num
            yield integer
            start_num += 1

    def halves():
        for i in integers():
            halve = i / 2
            yield halve

    def take(n, seq):
        result = []
        for el in seq:
            result.append(el)
            if len(result) == n:
                break
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

