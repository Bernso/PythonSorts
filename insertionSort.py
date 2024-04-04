import random
import os

os.system("cls")

listToSort = []

for i in range(0, 10):
    newValue = random.randint(1, 10)
    listToSort.append(newValue)

print(f"The list to sort is: \n{listToSort}")
print(f"\nThe length of the list is: {len(listToSort)}")


for i in range(1, len(listToSort)):
    key = listToSort[i]
    j = i - 1
    while j >= 0 and key < listToSort[j]:
        listToSort[j + 1] = listToSort[j]
        j -= 1
    listToSort[j + 1] = key



print(f"\nThe sorted list is: \n{listToSort}")