# link -> https://leetcode.com/problems/sample/

from leetcode import evaluate

class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        nowIn = []
        for char in s:
            if char in ["(", "{", "["]:
                nowIn.append(char)
            else:
                if not nowIn:
                    return False
                if char == charMap[nowIn[-1]]:
                    nowIn.pop(-1)
                else:
                    return False
        if nowIn:
            return False
        return True


if __name__ == "__main__":
    inputs = [
        ("()", ),
        ("()[]{}", ),
        ("(]", ),
        ("([])", ),
    ]
    outputs = [
        (True),
        (True),
        (False),
        (True),
    ]
    x = Solution()
    evaluate(x.isValid, inputs, outputs)
