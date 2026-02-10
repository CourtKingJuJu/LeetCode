class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
        num2 = 0
        num1 = 0

        i = 1
        while i <= n:
            if i % m == 0: 
                num2 += i
            else:
                num1 += i
            
            i += 1
        
        return num1 - num2