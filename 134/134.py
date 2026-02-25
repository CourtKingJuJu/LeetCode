class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(gas)
        difference = []
        
        for i in range(n):
            difference.append(gas[i] - cost[i])
        
        if sum(difference) < 0:
            return -1

        tank = 0
        sp = 0
        for i in range(n):
            tank+=gas[i]-cost[i]
            if tank<0:
                sp = i+1
                tank = 0

        return sp
        