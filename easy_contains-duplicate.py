from leetcode import evaluate

class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return True


if __name__ == "__main__":
    inputs = [
        ([1,2,3,1], ),
        ([1,2,3,4], ),
        ([1,1,1,3,3,4,3,2,4,2], ),
    ]
    outputs = [
        (True),
        (False),
        (True),
    ]
    x = Solution()
    evaluate(x.containsDuplicate, inputs, outputs)
