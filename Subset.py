def subset_sum(nums, target):
    n = len(nums)

   
    dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    
    for i in range(n + 1):
        dp[i][0] = True

   
    for i in range(1, n + 1):
        current_val = nums[i - 1]
        for j in range(1, target + 1):
            if j < current_val:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - current_val]

    
    found = dp[n][target]

   
    subset = []
    if found:
        i, j = n, target
        while i > 0 and j > 0:
            if dp[i][j] != dp[i - 1][j]:
                subset.append(nums[i - 1])
                j -= nums[i - 1]
            i -= 1

    return found, subset



numbers = [3, 2, 7, 1]
goal = 6

is_possible, result_set = subset_sum(numbers, goal)

print("Is sum possible?", is_possible)
if is_possible:
    print("Subset:", result_set)
