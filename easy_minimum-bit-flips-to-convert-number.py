from leetcode import evaluate

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        return bin(x).count('1')

if __name__ == "__main__":
    inputs = [
        (10, 7, ),
        (3, 4, ),
        (11, 100, ),
    ]
    outputs = [
        (3),
        (3),
        (3),
    ]
    x = Solution()
    evaluate(x.minBitFlips, inputs, outputs)
