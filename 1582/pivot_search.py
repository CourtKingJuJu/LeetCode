class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1

        ans = 0

        for row in range(len(rows)):
            for col in range(len(cols)):
                if mat[row][col] == 1 and rows[row] == 1 and cols[col] == 1:
                    ans += 1

        return ans