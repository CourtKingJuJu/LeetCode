class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        output = []
        
        # if 0,0 
            # increase J
        # if 0,n if j == n: 
            # increase i
        # if m,n 
            # decrease j
        # if m,0
            # decrease i
        
    
        # First row --> Last column --> last row --> first column 
        # (0,n) --> (m,n) --> (m,0) --> (0,0)
        rm = 0
        rx = len(matrix)-1
        cm = 0
        cx = len(matrix[0])-1

        while rm <= rx and cm <= cx:

            # Row min
            for j in range(len(matrix[0])):
                if matrix[rm][j] != None:
                    output.append(matrix[rm][j])
                    matrix[rm][j] = None
            rm += 1

            # Col max 
            for i in range(len(matrix)):
                if matrix[i][cx] != None:
                    output.append(matrix[i][cx])
                    matrix[i][cx] = None
            cx -= 1

            # Row Max
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[rx][j] != None:
                    output.append(matrix[rx][j])
                    matrix[rx][j] = None
            rx -= 1

            #Col Min
            for i in range(len(matrix) - 1, -1, -1):
                if matrix[i][cm] != None:
                    output.append(matrix[i][cm])
                    matrix[i][cm] = None
            cm += 1


        return output
    
    