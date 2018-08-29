# 560 Given an array of integers and an integer k, 
# you need to find the total number of continuous subarrays whose sum equals to k.

# Example:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Note:

# 1.The length of the array is in range [1, 20,000].
# 2.The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_arr = 0
        arr = []
        for i in nums:
            arr.append(i)
            if sum(arr) < k:
                continue
            elif sum(arr) == k:
                num_arr += 1
                del arr[0]
            else:
                while sum(arr) >= k and len(arr) > 1:
                    del arr[0]
                    if sum(arr) == k:
                        num_arr += 1
        return num_arr
		
# wrong:	only considering the num in array were positive number

# Traverse the array and add the numbers of the current position in turn, 
# and record the sum of all the numbers before the current position with the array sum, 
# so that the sum of the numbers between the subscripts [i, j] can be calculated with sum [j]-sum [i], 
# and then through a double-level loop, traverse all the cases to count the number of subarrays that meet the conditions.

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_arr = 0
        sum =[0]
        for i in range(0,len(nums)):
            b = sum[i] + nums[i]
            sum.append(b)
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                if (sum[j] - sum[i]) == k:
                    num_arr+=1
        return num_arr

# We can also use Hash Table to store the number of occurrences of sum. 
# If there are subarrays and total of sum-k before the current location,
# then the sum of the numbers between the two positions is k, 
# and the number of subarrays with the sum of the current position and the sum of K is hash [sum-k],
# so that the subarrays satisfying the conditions can be obtained the number by traversing the entire array.		

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_arr = 0
        tol = 0
        hash_ = {0:1}
        for i in nums:
            tol += i
            if (tol - k) in hash_:
                num_arr += hash_[tol - k]
            if tol not in hash_:
				hash_[tol] = 1
			else:
				hash_[tol] += 1
        return num_arr
		