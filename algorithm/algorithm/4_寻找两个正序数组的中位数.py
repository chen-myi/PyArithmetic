from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 中位数 奇数个数，排序后中间的数
        # 偶数个数，排序后中间两个数的均值
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)
        if n%2 == 0:
            return float(nums[n//2]+nums[n//2-1])/2
        else:
            return float(nums[n//2])

