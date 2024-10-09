from leetcode import evaluate

class Solution:
    def minSwaps(self, s: str) -> int:
        score, score_max = 0, 0
        for ss in s:
            if ss == "[":
                score -= 1
            else:
                score += 1
                score_max = max(score, score_max)
        return int(((score_max - 1) // 2) + 1)


if __name__ == "__main__":
    inputs = [
        ("][][", ),
        ("]]][[[", ),
        ("[]", ),
    ]
    outputs = [
        (1),
        (2),
        (0),
    ]
    x = Solution()
    evaluate(x.minSwaps, inputs, outputs)
