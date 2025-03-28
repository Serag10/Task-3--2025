
class Flight:
    def __init__(self, flight_id, time, altitude, speed):
        self.flight_id = flight_id
        self.time = time 
        self.altitude = altitude
        self.speed = speed

    def __repr__(self):
        return f"Flight({self.flight_id}, Time: {self.time}, Alt: {self.altitude}, Speed: {self.speed})"


def merge_sort(flights):
    if len(flights) <= 1:
        return flights

    mid = len(flights) // 2
    left_half = merge_sort(flights[:mid])
    right_half = merge_sort(flights[mid:])

    return merge(left_half, right_half)


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
    Flight("AA101", "12:30", 35000, 550),
    Flight("BA202", "10:15", 37000, 530),
    Flight("CC303", "14:45", 36000, 540),
    Flight("DD404", "09:00", 34000, 560)
]

sorted_flights = merge_sort(flights)

# Display sorted flights
for flight in sorted_flights:
    print(flight)
