class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        nums.sort()

        m = 0
        c = 0
        curr = nums[0]
        num = None

        for i in nums:
            if curr != i: 
                curr = i
                c = 0
            
            c += 1
            if c > m:
                m = c
                num = curr

        return num