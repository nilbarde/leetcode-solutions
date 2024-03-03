# link -> https://leetcode.com/problems/reverse-integer/

from leetcode import evaluate

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
            x = -x
        else:
            negative = False
        x = int(str(x)[::-1])
        if x >= 2 ** 31:
            return 0
        return -1 * x if negative else x


if __name__ == "__main__":
    inputs = [
        (123, ),
        (-123, ),
        (120, ),
        (1534236469, ),
    ]
    outputs = [
        (321),
        (-321),
        (21),
        (0),
    ]
    x = Solution()
    evaluate(x.reverse, inputs, outputs)
