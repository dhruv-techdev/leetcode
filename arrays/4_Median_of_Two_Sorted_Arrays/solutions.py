"""
4. Median of Two Sorted Arrays
Solved
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0

        merged_array = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1

        merged_array.extend(nums1[i:])
        merged_array.extend(nums2[j:])

        k = len(merged_array)
        if k % 2 == 0:
            median = (merged_array[k // 2] + merged_array[k // 2 - 1]) / 2
        else:
            median = merged_array[k // 2]

        return median


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([0, 0], [0, 0], 0.0),
        ([1, 3], [], 3.0),
        ([1, 2, 3], [4, 5, 6, 7], 4.0),
    ]

    for idx, (nums1, nums2, expected) in enumerate(test_cases, start=1):
        result = sol.findMedianSortedArrays(nums1, nums2)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {idx}: nums1={nums1}, nums2={nums2} -> got {result}, expected {expected} [{status}]")

"""
Input is 2 Sorted Arrays size m and n. We have to return the median of two sorted Arrays.

Input: num1 = [1,3] and num2 = [2]
output: 2.00000
Explanation: Merged array = [1,2,3] and median is (2+3) / 2 = 2.

Brute Force        
Math logic: 

For odd: median = merged[(m+n)//2]

For Even: median = ( merged[(m+n)//2] + merged[(m+n)//2 - 1] ) / 2

Replace the index with the value assigned

"""
