class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                output += nums[i]
            else:
                output -= nums[i]
        
        return output

