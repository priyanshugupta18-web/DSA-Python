#1. reversing an array 

#    ***********Normal value swapping through temp variable**********

# algorithm:-
from array import *

arr = array('i', [1, 2, 3, 4, 5, 6])

for i in range(len(arr)//2):
   
    temp = arr[i]
    arr[i] = arr[(len(arr)-(i+1))]
    arr[(len(arr)-(i+1))] = temp

for i in arr:
    print(i, end =" ")

# output: 6 5 4 3 2 1



#   *******Two pointer approach to reverse an array********

# Two pointers is a technique where we use two index variables (pointers) to traverse an array or list at the same time, instead of using nested loops.

# It is mainly used to reduce time complexity from O(n²) → O(n).

# 🧠 Basic Idea

# You keep:

# One pointer at the start

# Another pointer at the end (or both at start, depending on problem)

# Then move them based on a condition.

# algorithm:-
from array import *
arr = array('i', [1, 2, 3, 4, 5, 6])

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

for i in arr:
    print(i, end=" ")

# output: 6 5 4 3 2 1


#2. Find Minimum and Maximum element in an array

# approach:-
# Take the first element of arr as a reference for both minimum and maximum and then traverse through rest of the array and update the values and finally print them.

# algorithm:-
from array import *

arr = array('i', [4, 3, 7, 8, 9])

min = arr[0]
max = arr[0]

for i in range(1, len(arr)):
    if (arr[i] < min): 
        min = arr[i]
    if (arr[i] > max):
        max = arr[i]

print(f"The Minimum Value stored in arr is: {min}")
print(f"The Maximum Value stored in arr is: {max}")

#3. Sum of array elements

# approach:-
# create a variable for storing sum and calculate the sum of elements through iteration.

# algorithm:-
from array import *

arr = array('i', [1, 7, 5, 9])

sum = 0

for i in range(len(arr)):
    sum = sum + arr[i]

print(f"Sum of all elements of the array is: {sum}")

# 4. Check if Array is Sorted

# Task: Return True if array is sorted (ascending)
# Concept: Adjacent comparison

# approach:-
# Take a reference variable and intially pass value at 0th-index in the variable, then iterate through rest of the elements of the array and check that the element next to an element is greater than it or not, if yes then update the reference variable but if not then return false, we will also use check variable for checking if the array is sorted or not.

# algorithm:-
from array import *

def isSorted(arr):

    check = 1
    ref = arr[0]

    for i in range(1, len(arr)):
        if (arr[i] > ref):
            ref = arr[i]
        else:
            check = 0
            return False
    
    if (check == 1):
        return True

val_1 = array('i', [1, 2, 3, 4, 5])

print(f"The array is sorted in ascending order(True/False):{isSorted(val_1)}")

val_2 = array('i', [5, 3, 5, 6])

print(f"The array is sorted in ascending order(True/False):{isSorted(val_2)}")


# 5. Count Even and Odd Numbers

# Task: Count how many even and odd elements
# Concept: Modulo, traversal

# approach:-
# Declare two variables countEven and countOdd iterate through the array and then check even/odd and update the variables accordingly.

# algorithm:-
from array import *

val = array('i', [1, 2, 5, 7, 9])

countEven = 0
countOdd = 0

for i in val:
    if (i % 2 == 0):
        countEven += 1
    else:
        countOdd += 1
    
print(f"Number of Even elements = {countEven}")
print(f"Number of Odd elements = {countOdd}")

# 6. Linear Search

# Task: Find index of a given element
# Concept: Searching basics

# approach:-
# The approach is simple, we have defined a function and passing a value and an array as args then using iteration we are checking weather value = any element in the array, if yes then return the index, if no then return -1.

# algorithm:-
from array import *

def indexOf(key, arr):
    
    for i in range(len(arr)):
        if (arr[i] == key):
            return i
        
    return -1

val = array('i', [1, 2, 4, 67])
key = 67  

print(f"The index of the {key} in {val} = {indexOf(key, val)}")

# 7. Find Second Largest Element

# Task: Return second maximum element
# Concept: Variable tracking

# approach:-
# Declare two variable best and sec_best, store element at 0th index in best and -inf in sec_best, then iterate through the array with the help of two conditions, if arr[i] > best then assign arr[i] in best, if arr[i] < best but > sec_best, assign arr[i] to sec_best. finally return sec_best.

# algorithm:-

from array import *

def sec_best(arr):
    best = arr[0]
    sec_best = float('-inf')

    for i in range(1, len(arr)):
        if (arr[i] > best):
            sec_best = best
            best = arr[i]
        if ((arr[i] < best) and (arr[i] > sec_best)):
            sec_best = arr[i]
    
    return sec_best

arr = array('i', [23, 4, 7, 45, 1, 21])

print(f"The second largest element in the {arr} = {sec_best(arr)}")





