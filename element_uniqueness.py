# Algorithm: Element Uniqueness

# Input : An array A[0..n−1]
# Output: Return True if all elements in A are distinct,
#         otherwise return False
#
# Pseudocode:
# for i ← 0 to n − 2 do
#     for j ← i + 1 to n − 1 do
#         if A[i] = A[j] then
#             return false
# return true
# ---------------------------------------------


def element_uniqueness(A):
    n = len(A)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                return False
    return True


A = list(map(int, input("Enter elements separated by space: ").split()))
print(element_uniqueness(A))
