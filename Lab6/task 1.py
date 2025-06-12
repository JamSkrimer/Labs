list = ['Артём', 'Денис', 'Абоба', 'Максим', 'Алег', 'Олег', 'Илья', 'Сергей', 'Вергилий', 'ОН']
A_names = []
for i in list:
    for j in i:
        if j[0] == 'А':
            A_names.append(i)
print(A_names)