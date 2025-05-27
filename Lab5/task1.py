def calc_sum(n):
    return sum(range(1, n + 1))
n = int(input("Введите число N: "))
result = calc_sum(n)

print(f"Сумма чисел от 1 до {n} = {result}")
