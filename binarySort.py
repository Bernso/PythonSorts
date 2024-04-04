import random
import os

os.system("cls")

def binary_search(arr, val, start, end):
    # We need to distinugish whether we should insert before or after the left boundary.
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    # If the array is empty, insert the value at the start
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

listToSort = []
for i in range(0, 100):
    newValue = random.randint(1, 100)
    listToSort.append(newValue)


print(f"Starting list: {listToSort}")

print(f"\nThe length of the list is: {len(listToSort)}")

sorted_list = binary_sort(listToSort)
print("\nSorted list:", sorted_list)


# I did not write this code.