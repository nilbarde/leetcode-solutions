from leetcode import evaluate

class Solution:
    def majorityElement(self, nums) -> int:
        element, count = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == element:
                count += 1
            else:
                count -= 1
                if count < 0:
                    element = nums[i]
                    count = 1
        return element


if __name__ == "__main__":
    inputs = [
        ([3, 2, 3], ),
        ([2, 2, 1, 1, 1, 2, 2], ),
    ]
    outputs = [
        (3),
        (2),
    ]
    x = Solution()
    evaluate(x.majorityElement, inputs, outputs)
