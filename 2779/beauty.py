class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
            # move one untill you get into the subset

         
        best = 1
        nums = sorted(nums)

        i = 0
        j = 1
        while j < len(nums):

            if nums[j] - nums[i] <= 2 * k:
                if best < j - i + 1:
                    best = j - i + 1
                j += 1

            else:
                i += 1            


        return best

