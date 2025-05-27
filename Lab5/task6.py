def change_signs(arr):
    return [-x for x in arr]
array = [1, -5, 0, 3, -4]
modified_array = change_signs(array)
print(f"Массив после замены знаков: {modified_array}")
