class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        DP = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                else: 
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])

        print(DP)
        return DP[len(text1)][len(text2)]
    #    '''
    #    ace, abcde 

    # i    a c e
    # 0  a x 0 0
    # 1  b 0
    #    c 0 x
    #    d 0
    #    e 0   x
    #    '''