class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for el in args:
            result *= el
        return result

    @staticmethod
    def divide(*args):
        result = 0
        for i in range(len(args) - 1):
            if i == 0:
                result = args[i] / args[i + 1]
            else:
                result /= args[i + 1]
        return result

    @staticmethod
    def subtract(*args):
        result = 0
        for i in range(len(args) - 1):
            if i == 0:
                result = args[i] - args[i + 1]
            else:
                result -= args[i + 1]
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

