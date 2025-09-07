'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1