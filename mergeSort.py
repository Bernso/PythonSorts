import random
import os

os.system("cls")

listToSort = []

for i in range(0, 100):
    newValue = random.randint(1, 100)
    listToSort.append(newValue)

print(f"The list to sort is: \n{listToSort}")
print(f"The length of the list is: {len(listToSort)}")


if len(listToSort) <= 1:
    print("The list is too short")
    quit()

else:
    half1LowerValue = 0
    half1UpperValue = len(listToSort)/2
    half2LowerValue = len(listToSort)/2
    half2UpperValue = len(listToSort)
    
    half1 = listToSort[int(half1LowerValue):int(half1UpperValue)]
    half2 = listToSort[int(half2LowerValue):int(half2UpperValue)]
    print(f"\nThe first half of the list is: \n{half1}")
    print(f"The second half of the list is: \n{half2}")

    half1.sort()
    half2.sort()
    
    listToSort = half1 + half2
    print(f"\nThe list when they have just been combined: \n{listToSort}")
    
    listToSort.sort()
        

print(f"\nThe sorted list is: \n{listToSort}")