# First attempt, Issure runtime 
'''
class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        # Flip to check palidrome
        def flip(num):
            return str(num)[::-1]

        # Conver to base k
        def convert(num):
            converted = ''

            while num != 0:
                converted += str(num % k)
                num //= k

            return converted


        # sum bsum then subtract 1 from n
        # Because we found a solution
        bsum = 0

        i = 1
        while n != 0:
            if str(i) == flip(i):
                nk = convert(i)

                if nk == flip(nk):
                    bsum += i
                    n -= 1

            i += 1
        
        return bsum
'''