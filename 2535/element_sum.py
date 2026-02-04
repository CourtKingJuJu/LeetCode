class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        elementSum = 0
        digitSum = 0

        for i in range(len(nums)):
            curr_element = nums[i]
            elementSum += curr_element

            while curr_element >= 10: 
                digitSum += curr_element % 10
                curr_element = curr_element // 10

            digitSum += curr_element

        return abs(elementSum - digitSum)