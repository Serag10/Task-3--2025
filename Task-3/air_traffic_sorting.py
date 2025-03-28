# Air Traffic Control Sorting Problem

class Flight:
    def __init__(self, flight_id, time, altitude, speed):
        self.flight_id = flight_id
        self.time = time  # Arrival or departure time (in hour:minute format)
        self.altitude = altitude
        self.speed = speed

    def __str__(self):
        return f"ID: {self.flight_id}, Time: {self.time}, Alt: {self.altitude}, Speed: {self.speed}"

# QuickSort partition function
def partition(flights, low, high):
    pivot = flights[high].time  # We choose time as the standard for comparison.
    i = low - 1
    for j in range(low, high):
        if flights[j].time <= pivot:
            i += 1
            flights[i], flights[j] = flights[j], flights[i]
    flights[i + 1], flights[high] = flights[high], flights[i + 1]
    return i + 1

# QuickSort main function
def quicksort(flights, low, high):
    if low < high:
        pi = partition(flights, low, high)
        quicksort(flights, low, pi - 1)
        quicksort(flights, pi + 1, high)

# =================================================================

# Test the solution
flights = [
    Flight("AA123", "14:30", 35000, 500),
    Flight("BA456", "13:45", 30000, 480),
    Flight("CA789", "15:00", 37000, 520),
    Flight("DA101", "14:00", 32000, 490)
]

print("Before sorting:")
for flight in flights:
    print(flight)

print("\n-----------------------------------\n")

# Perform sorting
quicksort(flights, 0, len(flights) - 1)

print("After sorting by time:")
for flight in flights:
    print(flight)