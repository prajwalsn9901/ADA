def selection_sort(arr):
    n=len(arr)

    for i in range(n-1):
        min_index=1

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j

        arr[i], arr[min_index] = arr[min_index]


n = int(input("Enter the value of n:"))
l = []

for i in range(n):
    l.append(int(input(f"Enter element {i+1}:")))

selection_sort(l)
print("sorted list:",1)
