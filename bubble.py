import random

def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
               arr[j],arr[j+1] = arr[j+1],arr[j]
n = 5000
l = [random.randint(1,10000)for i in range(n)]

bubble_sort(l)
print("sorted list:",l)
