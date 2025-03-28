
def insertion_sort(patients):

    for i in range(1, len(patients)):
        key = patients[i]  
        j = i - 1
        while j >= 0 and patients[j][1] < key[1]:  
            patients[j + 1] = patients[j]
            j -= 1
        patients[j + 1] = key

patients = [
    ("Ahmed", 180),
    ("Sara", 90),
    ("Omar", 220),
    ("Layla", 110),
    ("Khaled", 150),
    ("Youssef", 250),
    ("Fatima", 85),
    ("Mahmoud", 195),
    ("Amina", 140),
    ("Hassan", 175)
]

insertion_sort(patients)

print("For patients prioritized (highest risk first):")
for name, sugar in patients:
    print(f"{name}: {sugar} mg/dL")
