from leetcode import evaluate

from collections import defaultdict

class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        # print(jobs)
        maxProfit = defaultdict(int)
        for i in range(len(startTime) - 1, -1, -1):
            maxProfit[jobs[i][0]] = max(maxProfit[jobs[i][0]], jobs[i][2] + maxProfit[jobs[i][1]])
            maxProfit[jobs[i][0]] = max(maxProfit[jobs[i][0]], maxProfit[jobs[i][0] + 1])
            if i:
                for j in range(jobs[i][0], jobs[i-1][0], -1):
                    maxProfit[j] = maxProfit[jobs[i][0]]
        # print(maxProfit)
        return maxProfit[jobs[0][0]]

if __name__ == "__main__":
    inputs = [
        ([1,2,3,3], [3,4,5,6], [50,10,40,70]),
        ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]),
        ([1,1,1], [2,3,4], [5,6,4]),
        ([6,15,7,11,1,3,16,2], [19,18,19,16,10,8,19,8], [2,9,1,19,5,7,3,19]),
    ]
    outputs = [
        (120),
        (150),
        (6),
        (41),
    ]
    x = Solution()
    evaluate(x.jobScheduling, inputs, outputs)
