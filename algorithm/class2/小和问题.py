def merge_sum(arr, left, right):
    if left == right:
        return 0
    mid = left + ((right - left) >> 1)
    return merge_sum(arr, left, mid) + merge_sum(arr, mid + 1, right)+ merge(arr, left, mid, right)
def merge(arr, left, mid, right):
    help = []
    l1 = left
    l2 = mid + 1
    res = 0
    while l1 <= mid and l2 <= right:
        if arr[l1] < arr[l2]:
            res = res + arr[l1] * (right - l2 + 1)
            help.append(arr[l1])
            l1 = l1 + 1
        else:
            res = res + 0
            help.append(arr[l2])
            l2 = l2 + 1
    while l1 <= mid:
        help.append(arr[l1])
        l1 = l1 + 1
    while l2 <= right:
        help.append(arr[l2])
        l2 = l2 + 1
    for i in range(len(help)):
        arr[left + i] = help[i]
    return res

arr = [12, 11, 13, 5, 6, 7]
print(merge_sum(arr, 0, len(arr) - 1))
print(arr)