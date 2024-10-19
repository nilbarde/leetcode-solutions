from leetcode import evaluate
import math

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flips = 0
        power2 = 2 ** int(math.log(k, 2))
        while power2 != k:
            k = 2 * power2 - k
            power2 = 2 ** int(math.log(k, 2))
            flips += 1
        if power2 == 1:
            if flips % 2 == 0:
                return "0"
            else:
                return "1"
        else:
            if flips % 2 == 0:
                return "1"
            else:
                return "0"
            

if __name__ == "__main__":
    inputs = [
        (3, 1, ),
        (4, 11, ),
        (4, 1, ),
        (4, 2, ),
        (4, 3, ),
        (4, 4, ),
        (4, 5, ),
        (4, 6, ),
        (4, 7, ),
        (4, 8, ),
        (4, 9, ),
        (4, 10, ),
        (4, 11, ),
        (4, 12, ),
        (4, 13, ),
        (4, 14, ),
        (4, 15, ),
    ]
    outputs = [
        ("0"),
        ("1"),
        ("0"),
        ("1"),
        ("1"),
        ("1"),
        ("0"),
        ("0"),
        ("1"),
        ("1"),
        ("0"),
        ("1"),
        ("1"),
        ("0"),
        ("0"),
        ("0"),
        ("1"),
    ]
    x = Solution()
    evaluate(x.findKthBit, inputs, outputs)
"""
  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
  0  1  1  1  0  0  1  1  0  1  1  0  0  0  1
   0
 011
1001

"""