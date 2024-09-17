data = []
results = {}
while True:
    in_data = input()
    if not in_data:
        break
    data.append(in_data)
    
for d in data:
    lesson, f, mark = d.split()
    if lesson not in results:
        results[lesson] = {}
    if f not in results[lesson]:
        results[lesson][f] = []
    results[lesson][f].append(mark)

for lesson, fs in results.items():
    print(lesson)
    for f, marks in fs.items():
        print(f"{f} {' '.join(marks)}")
    print()
