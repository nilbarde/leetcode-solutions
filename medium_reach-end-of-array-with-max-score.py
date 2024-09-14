from leetcode import evaluate

class Solution:
    def findMaximumScore(self, nums) -> int:
        current_max, current_start = nums[0], 0
        answer = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > current_max:
                answer += current_max * (i - current_start)
                current_max = nums[i]
                current_start = i
        answer += current_max * (len(nums) - 1 - current_start)
        return answer


if __name__ == "__main__":
    inputs = [
        ([1,3,1,5], ),
        ([4,3,1,3,2], ),
    ]
    outputs = [
        (7),
        (16),
    ]
    x = Solution()
    evaluate(x.findMaximumScore, inputs, outputs)
