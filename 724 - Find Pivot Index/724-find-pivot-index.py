'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
 

Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].


Name: NaiveSolution
Runtime: O(N^2)
About: The following naive solution will fail on test case 732/741.
Status: "Time Limit Exceeded".

class NaiveSolution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # store the length of the array. 
        arr_len = len(nums)
        
        # iterate over each possible pivot index. 
        for pivot in range(0, arr_len):

            # init the sum variable for left side of pivot. 
            sum_left = 0
            
            # sum the left side of the pivot.
            for left_pos in range(0, pivot):
                sum_left += nums[left_pos]
            
            # init the sum variable for right side of pivot. 
            sum_right = 0
            
            # sum the right side of the pivot.
            for right_pos in range(pivot + 1, arr_len):
                sum_right += nums[right_pos]

            # check if left and right side sums are equal. 
            if sum_left == sum_right: 
                return pivot

        return -1

Name: Solution
Runtime: 0(N)
About: The following optimized solution passed 741 / 741 test cases.
Status: "Accepted".

'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # store the length of the array. 
        arr_len = len(nums)
        
        # init the sum variable for the left side of the pivot. 
        sum_left = 0

        # init the sum variable for the right side of the pivot. 
        sum_right = sum(nums)

        # iterate over each possible pivot index. 
        for pivot in range(0, arr_len):

            # if there is a value to the left side of the pivot. 
            # add it to the sum of the left side.
            if pivot - 1 >= 0:
                sum_left += nums[pivot - 1]

            # remove the value of the pivot from the right side sum.
            sum_right -= nums[pivot]

            # check if the left side and right side sums are equal.
            # if so, return pivot index.
            if sum_left == sum_right:
                return pivot
        
        # no solution, return -1.
        return -1