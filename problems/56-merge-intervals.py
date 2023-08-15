class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort based on start time
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1] = [output[-1][0], max(end, output[-1][1])]
            else:
                output.append([start, end])
        return output