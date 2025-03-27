def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[1] < pivot[1]]
    middle = [x for x in arr if x[1] == pivot[1]]
    right = [x for x in arr if x[1] > pivot[1]]
    return quick_sort(left) + middle + quick_sort(right)

# Sample flight data (Flight ID, Time, Altitude, Speed)
flights = [
    ("F101", "12:30", 30000, 500),
    ("F205", "08:45", 28000, 520),
    ("F330", "14:15", 32000, 480),
    ("F120", "09:10", 29000, 510),
    ("F450", "10:30", 31000, 530)
]

# Convert time to minutes for easy comparison
flights = [(f[0], int(f[1].split(":")[0]) * 60 + int(f[1].split(":")[1]), f[2], f[3]) for f in flights]

# Sort flights by arrival/departure time
sorted_flights = quick_sort(flights)

# Convert time back to original format and display results
sorted_flights = [(f[0], f"{f[1] // 60:02d}:{f[1] % 60:02d}", f[2], f[3]) for f in sorted_flights]

print("Flights sorted by time:")
for flight in sorted_flights:
    print(flight)
