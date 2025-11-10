nums = [5,2,4,3,2]
nums_sorted = nums.copy()
switches = len(nums) - 1

print(switches)

for i in range(switches):
    flag = True
    for j in range(switches - i):
        if nums_sorted[j] > nums_sorted[j + 1]:
            nums_sorted[j], nums_sorted[j + 1] = nums_sorted[j + 1], nums_sorted[j]
            flag = False
    if flag: break

print(nums, nums_sorted)
        