'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].

Name: Solution
Runtime: 0(N)
About: The following optimized solution passed 250 / 250 test cases.
Status: "Accepted".

'''

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        # store the length of the array.
        arr_len = len(nums)
        
        # initialize largest index, largest num and second largest num.
        largest_index = -1 
        
        largest_num = -1
        second_largest_num = -1
        
        
        # iterate over each number.
        for i in range(0, arr_len):
            
            # if the current number is the largest so far,
            # set as new biggest, and update largest index.
            # also, we need to update second largest.
            if nums[i] > largest_num:
                temp = largest_num
                largest_num = nums[i]
                second_largest_num = temp
                largest_index = i
            
            # if may not be the largest number,
            # but largest than the second biggest.
            elif nums[i] > second_largest_num:
                second_largest_num = nums[i]
            
        # at least twice check.
        # return index if check passed.
        if second_largest_num * 2 <= largest_num:
            return largest_index
        
        # no answer.
        return -1