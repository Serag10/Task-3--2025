class Flight:
    def __init__(self, flight_id, time, altitude, speed):
        self.flight_id = flight_id
        self.time = time  
        self.altitude = altitude
        self.speed = speed
    
    def __repr__(self):
        return f"({self.flight_id}, {self.time}, {self.altitude}, {self.speed})"

def merge_sort(flights):
    if len(flights) <= 1:
        return flights
    
    mid = len(flights) // 2
    left = merge_sort(flights[:mid])
    right = merge_sort(flights[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i].time <= right[j].time:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

flights = [
    Flight("A101", 15, 30000, 500),
    Flight("B202", 10, 32000, 550),
    Flight("C303", 20, 31000, 530),
    Flight("D404", 5, 29000, 490),
]

sorted_flights = merge_sort(flights)

print("Sorted Flights (by time):")
for flight in sorted_flights:
    print(flight)
