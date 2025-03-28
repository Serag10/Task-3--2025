def quick_sort(patients):
    if len(patients) <= 1:
        return patients
    
    pivot = patients[len(patients) // 2][1]
    left = [p for p in patients if p[1] > pivot]
    middle = [p for p in patients if p[1] == pivot]
    right = [p for p in patients if p[1] < pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

patients = [
    ("Ahmed", 12, 30, 30),
    ("Sara", 8, 15, 25),
    ("Omar", 20, 50, 40),
    ("Layla", 5, 10, 20),
    ("Khaled", 18, 40, 35),
    ("Youssef", 10, 25, 28),
    ("Fatima", 22, 55, 45)
]

growth_rates = [(name, (current - initial) / days) for name, initial, current, days in patients]

sorted_patients = quick_sort(growth_rates)

top_3 = sorted_patients[:3]

print("Top 3 fastest-growing tumors:")
for name, rate in top_3:
    print(name, ":", rate)
