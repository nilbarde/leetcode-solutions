from leetcode import evaluate

class Solution:
    def findMinDifference(self, timePoints) -> int:
        timestamps = [self.getTimestamp(time) for time in timePoints]
        timestamps.sort()
        minDiff = 24*60
        dayDiff = 24*60
        for i in range(len(timestamps)-1):
            diff = timestamps[i+1] - timestamps[i]
            minDiff = min(minDiff, diff)
            diff = dayDiff - diff
            minDiff = min(minDiff, diff)

        diff = timestamps[-1] - timestamps[0]
        minDiff = min(minDiff, diff)
        diff = dayDiff - diff
        minDiff = min(minDiff, diff)

        return minDiff

    def getTimestamp(self, time):
        h, m = time.split(":")
        return int(h) * 60 + int(m)

if __name__ == "__main__":
    inputs = [
        (["23:59","00:00"], ),
        (["00:00","23:59","00:00"],),
        (["00:00","04:00","22:00"], )
    ]
    outputs = [
        (1),
        (0),
        (120),
    ]
    x = Solution()
    evaluate(x.findMinDifference, inputs, outputs)
