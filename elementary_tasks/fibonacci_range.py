def fibonacci(n):
    # Считает число Фибоначчи
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_generation(s, f):
    # Генерирует числа Фибоначчи в указанном диапазоне
    fibonacci_list = []
    for n in range(s, f + 1):
        fibonacci_number = fibonacci(n)
        fibonacci_list.append(fibonacci_number)
    return fibonacci_list


start = int(input())
finish = int(input())
fibonacci_range = fibonacci_generation(start, finish)
fibonacci_range = [str(_) for _ in fibonacci_range]
fibonacci_range = ', '.join(fibonacci_range)
print(fibonacci_range)
