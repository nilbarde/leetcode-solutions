from leetcode import evaluate

class Solution:
    possible_options = ["AB", "CD"]
    def minLength(self, s: str) -> int:
        for opt in self.possible_options:
            if opt in s:
                i = s.index(opt)
                return self.minLength(s[:i] + s[i+2:])
        return len(s)


if __name__ == "__main__":
    inputs = [
        ("ABFCACDB", ),
        ("ACBBD", ),
    ]
    outputs = [
        (2),
        (5),
    ]
    x = Solution()
    evaluate(x.minLength, inputs, outputs)
