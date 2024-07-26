# 在一个范围上求数组最大值
def get_max(num, left, right):
    if right < left:
        return None
    if right == left:
        return num[right]
    # 求中点
    mid = left + ((right - left) >> 2)
    left_max = get_max(num, left, mid)
    right_max = get_max(num, mid + 1, right)
    return max(left_max, right_max)

