data = [
    {"ID": "A1", "Time": "14:20", "Value": 390},
    {"ID": "B2", "Time": "12:45", "Value": 320},
    {"ID": "C3", "Time": "16:10", "Value": 410},
    {"ID": "D4", "Time": "11:30", "Value": 300},
]

def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if time_to_minutes(left[i][key]) < time_to_minutes(right[j][key]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

sorted_data = merge_sort(data, "Time")

for item in sorted_data:
    print(f"ID {item['ID']} - Time: {item['Time']} - Value: {item['Value']}")
