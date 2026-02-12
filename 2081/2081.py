class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """

        # Conver to base k
        def convert(num):
            converted = ''
            while num != 0:
                converted += str(num % k)
                num //= k
            return converted
    
        bsum = 0
        length = 1
        count = 0
        
        while count < n:
            for i in range(10**(length-1), 10**length):
                s = str(i)
                num_str = s + s[:-1][::-1]
                num = int(num_str)
                basek_num = convert(num)
                if basek_num == basek_num[::-1]:
                    count += 1
                    bsum += num
                    if count == n: return bsum
        
            for i in range(10**(length-1), 10**length):
                s = str(i)
                num_str = s + s[::-1]
                num = int(num_str)
                basek_num = convert(num)
                if basek_num == basek_num[::-1]:
                    count += 1
                    bsum += num
                    if count == n: return bsum


            length += 1

        return bsum

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