class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        output = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                ind, temp = stack.pop()
                output[ind] = (i - ind)
            stack.append([i, t])    
        return output