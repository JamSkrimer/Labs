import datetime, random


class Task:
    def __init__(self, DateStart, DateFinish, Description):
        self.DateStart = DateStart
        self.DateFinish = DateFinish
        self.Description = Description

task = []

for i in range(5):
    start = datetime.datetime(2025, random.randint(1, 12), random.randint(1, 12))
    task.append(Task(start, start + datetime.timedelta(days=1), 'Люто date крч'))
end_date = 0
for i in range(len(task)):
    print(task[end_date].DateStart, task[end_date].DateFinish,task[end_date].Description)
    if task[i].DateFinish > task[end_date].DateFinish:
        end_date = i
print("\n", task[end_date].DateStart, task[end_date].DateFinish, task[end_date].Description)