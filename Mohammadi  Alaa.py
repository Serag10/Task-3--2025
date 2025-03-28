import datetime

def merge_sort(flight_list):
    if len(flight_list) <= 1:
        return flight_list
    
    mid_index = len(flight_list) // 2
    left_half = merge_sort(flight_list[:mid_index])
    right_half = merge_sort(flight_list[mid_index:])
    
    return merge(left_half, right_half)

def merge(left_half, right_half):
    sorted_list = []
    left_index = right_index = 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index]['time'] <= right_half[right_index]['time']:
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1
    
    sorted_list.extend(left_half[left_index:])
    sorted_list.extend(right_half[right_index:])
    
    return sorted_list

flight_list = [
    {"flight_id": "AA123", "time": datetime.datetime(2025, 3, 23, 14, 30), "altitude": 35000, "speed": 550},
    {"flight_id": "BA456", "time": datetime.datetime(2025, 3, 23, 12, 45), "altitude": 37000, "speed": 580},
    {"flight_id": "QR789", "time": datetime.datetime(2025, 3, 23, 16, 10), "altitude": 36000, "speed": 560},
    {"flight_id": "EK101", "time": datetime.datetime(2025, 3, 23, 11, 20), "altitude": 34000, "speed": 540}
]

print("Before : ")
for flight in flight_list:
    print(f"{flight['flight_id']} - {flight['time']}")

sorted_flight_list = merge_sort(flight_list)

print("After sorting by arrival/departure time :")
for flight in sorted_flight_list:
    print(f"{flight['flight_id']} - {flight['time']}")
