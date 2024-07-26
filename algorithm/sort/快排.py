import random
def partation(arr, left, right):
    # <区域的右边界
    l1 = left - 1
    # >区域的左边界
    r1 = right
    while left < r1:
        if arr[left] < arr[right]:
            l1 += 1
            arr[l1], arr[left] = arr[left], arr[l1]
            left += 1
        elif arr[left] > arr[right]:
            r1 -= 1
            arr[left], arr[r1] = arr[r1], arr[left]
        else:
            left += 1
    arr[r1], arr[right] = arr[right], arr[r1]
    return [l1 + 1, r1]
def rapid_typesetting(arr, left, right):
    if right > left:
        ran = left + random.randint(0, right - left)
        arr[ran], arr[right] = arr[right], arr[ran]
        p = partation(arr, left, right)
        rapid_typesetting(arr, left, p[0] - 1)
        rapid_typesetting(arr, p[1]+1, right)

arr = [1, 4, 3, 23, 4, 23, 2, 3, 5]
rapid_typesetting(arr, 0, len(arr)-1)
print(arr)

