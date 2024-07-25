# 问：现有一个数组，其中有两个数出现了奇数次，其他的都出现了偶数次，找出这两个数字，要求算法时间复杂度不超过O(N)
arr = [12, 12, 23, 23, 34, 23, 45, 45, 6, 6]
i = 0
only_one = 0
for e in arr:
    i = i ^ e
right_one = i & (~i+1)
for e in arr:
    if (e & right_one) == 0:
        only_one = only_one ^ e
print(only_one)
print(only_one^i)
