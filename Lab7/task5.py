class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

    def __str__(self):
        return f"Клиент: {self.client_code}, Год: {self.year}, Месяц: {self.month}, Продолжительность: {self.duration} мин"

fitness_list = [
    FitnessCenter("001", 2025, 1, 1000),
    FitnessCenter("002", 2024, 2, 38),
    FitnessCenter("003", 2026, 3, 75),
    FitnessCenter("004", 2022, 4, 345),
    FitnessCenter("005", 3000, 5, 75),
    FitnessCenter("006", 2001, 6, 1200),
    FitnessCenter("007", 2024, 7, 9),
    FitnessCenter("008", 2023, 8, 200),
    FitnessCenter("009", 2000, 9, 1250),
    FitnessCenter("010", 2020, 11, 180)
]

print("Список клиентов фитнес-центра:")
for i, client in enumerate(fitness_list, 1):
    print(f"{i}. {client}")

longest = max(fitness_list, key=lambda x: x.duration)
shortest = min(fitness_list, key=lambda x: x.duration)
print("\nИнформация о занятиях:")
print(f"Самое продолжительное занятие: {longest}")
print(f"Самое короткое занятие: {shortest}")

year_totals = {}
for session in fitness_list:
    year_totals[session.year] = year_totals.get(session.year, 0) + session.duration

max_duration = max(year_totals.values())
best_year = min(year for year, duration in year_totals.items() if duration == max_duration)

print(f"\nГод с наибольшей суммарной продолжительностью: {best_year}")
print(f"Суммарная продолжительность: {max_duration} мин")

print(f"\nСуммарная продолжительность по годам:")
for year in sorted(year_totals.keys()):
    print(f"Год {year}: {year_totals[year]} мин")