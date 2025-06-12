class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

    def __str__(self):
        return f"Клиент: {self.client_code}, Год: {self.year}, Месяц: {self.month}, Продолжительность: {self.duration} мин"

def find_duration_extremes(fitness_list):
    longest = max(fitness_list, key=lambda x: x.duration)
    shortest = min(fitness_list, key=lambda x: x.duration)
    print("\nИнформация о занятиях: ")
    print(f"Самое продолжительное занятие: {longest}")
    print(f"Самое короткое занятие:  {shortest}")
    return longest, shortest

fitness_list = [
    FitnessCenter("001", 2025, 1, 1000),
    FitnessCenter("002", 2024, 2, 38),
    FitnessCenter("003", 2026, 1, 75),
    FitnessCenter("004", 2022, 3, 345),
    FitnessCenter("005", 3000, 2, 75)
]

print("Список клиентов фитнес-центра:")
for i, client in enumerate(fitness_list, 1):
    print(f"{i}. {client}")

find_duration_extremes(fitness_list)
