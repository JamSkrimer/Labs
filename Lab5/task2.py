def petya_homework(numbers):
    positive_sum = sum(num for num in numbers if num > 0)
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)
    product = 1

    for i in range(start, end):
        product *= numbers[i]

    return positive_sum, product

test_cases = [
    [1, 2, 3, 4, 5, 6, 7],
    [7, 6, 5, -1, 8, 4],
    [11, -5, 3, 8, -3, 6, 1],
]

for i in range(len(test_cases)):
    arr = test_cases[i]
    pos_sum, prod = petya_homework(arr)
    print(f"Тест номер{i+1}: {arr}")
    print(f"Сумма положительных: {pos_sum}, Произведение: {prod}")
    print("-" * 30)