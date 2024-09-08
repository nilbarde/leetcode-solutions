from leetcode import evaluate

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]

if __name__ == "__main__":
    inputs = [
        ("11", "1", ),
        ("1010", "1011", ),
    ]
    outputs = [
        ("100"),
        ("10101"),
    ]
    x = Solution()
    evaluate(x.addBinary, inputs, outputs)
