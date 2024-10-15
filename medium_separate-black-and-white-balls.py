from leetcode import evaluate

class Solution:
    def minimumSteps(self, s: str) -> int:
        ball0faced = 0
        steps = 0
        for i, ball in enumerate(s):
            if ball == "0":
                steps += i - ball0faced
                ball0faced += 1
        return steps


if __name__ == "__main__":
    inputs = [
        ("101", ),
        ("100", ),
        ("0111", ),
    ]
    outputs = [
        (1),
        (2),
        (0),
    ]
    x = Solution()
    evaluate(x.minimumSteps, inputs, outputs)
