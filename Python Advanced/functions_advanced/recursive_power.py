def recursive_power(num, power, result=[]):
    if power == 0:
        return
    result.append(num)
    num *= result[0]
    recursive_power(num, power - 1)
    result_num = result.pop(0)
    return result_num


print(recursive_power(2, 10))
print(recursive_power(10, 100))