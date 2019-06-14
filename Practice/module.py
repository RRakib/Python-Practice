def kg_to_pound(kg):
    return kg / .45


def pound_to_kg(pound):
    return pound * .45


def find_max_number(inputValue):
    max_numer = int(inputValue[0])

    for numbers in inputValue:
        number = int(numbers)
        if number > max_numer:
            max_numer = number

    return max_numer


def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    print(result)

#### Now import this file without extention on other file to access the functions
