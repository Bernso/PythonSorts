import random
import os

os.system("cls")

listToSort = []

for i in range(0, 10):
    newValue = random.randint(1, 10)
    listToSort.append(newValue)

print(f"The list to sort is: \n{listToSort}")
print(f"\nThe length of the list is: {len(listToSort)}")



    
for i in range(0, len(listToSort) - 1):
    
    if listToSort[i] > listToSort[i + 1]:
        
        temp = listToSort[i]
        listToSort[i] = listToSort[i + 1]
        listToSort[i + 1] = temp

        

print(f"\nThe sorted list is: \n{listToSort}")