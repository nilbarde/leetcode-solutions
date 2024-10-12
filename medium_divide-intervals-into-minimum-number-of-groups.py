from leetcode import evaluate

class Solution:
    def minGroups(self, intervals) -> int:
        actions = []
        for interval in intervals:
            actions.append((interval[0], 0, 1))
            actions.append((interval[1], 1, -1))
        actions.sort()

        maxGroups = 0
        nowVal = 0
        for action in actions:
            nowVal += action[2]
            maxGroups = max(maxGroups, nowVal)

        return maxGroups

if __name__ == "__main__":
    inputs = [
        ([[5,10],[6,8],[1,5],[2,3],[1,10]], ),
        ([[1,3],[5,6],[8,10],[11,13]], ),
    ]
    outputs = [
        (3),
        (1),
    ]
    x = Solution()
    evaluate(x.minGroups, inputs, outputs)
