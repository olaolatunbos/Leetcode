class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # add interval
        intervals.append(newInterval)

        # sort intevals
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1] = [output[-1][0], max(output[-1][1], end)]
            else:
                output.append([start, end])
        return output

