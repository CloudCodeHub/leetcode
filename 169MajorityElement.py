# 169 Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example:
# Input: [3,2,3]
# Output: 3

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_ele = 0
        flag = 0
        for i in nums:
            if flag == 0:
                maj_ele = i
                flag += 1
            elif maj_ele == i:
                flag += 1
            else:
                flag -= 1
        return maj_ele