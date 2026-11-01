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

"""
Approach: Brute Force (Two Pointer Merge)

Both arrays are already sorted, so walk through them with two pointers
i and j, always taking the smaller value. This builds the fully sorted
merged array, the same way the merge step of merge sort works.

Math logic:

Total length k = m + n

For odd k:  median = merged[k // 2]
For even k: median = ( merged[k // 2 - 1] + merged[k // 2] ) / 2

Walkthrough:

nums1 = [1,3], nums2 = [2]
merged = [1,2,3], k = 3 (odd), k // 2 = 1
median = merged[1] = 2

nums1 = [1,2], nums2 = [3,4]
merged = [1,2,3,4], k = 4 (even), k // 2 = 2
median = ( merged[1] + merged[2] ) / 2 = (2 + 3) / 2 = 2.5

Complexity: Time O(m + n), Space O(m + n)
Note: the problem asks for O(log (m+n)), which needs binary search on the
partition. This merge version is the simpler brute force.
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
