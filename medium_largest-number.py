from leetcode import evaluate

class Solution:
    def largestNumber(self, nums) -> str:
        nums = list(map(str, nums))
        return str(int("".join(reversed(sorted(nums, key=lambda x: x*9)))))


if __name__ == "__main__":
    inputs = [
        ([10,2], ),
        ([3,30,34,5,9], ),
    ]
    outputs = [
        ("210"),
        ("9534330"),
    ]
    x = Solution()
    evaluate(x.largestNumber, inputs, outputs)
