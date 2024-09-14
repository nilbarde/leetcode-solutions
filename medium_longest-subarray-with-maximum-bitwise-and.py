from leetcode import evaluate

class Solution:
    def longestSubarray(self, nums) -> int:
        current_max, current_occ, longest_occ = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] > current_max:
                current_max = nums[i]
                current_occ = 1
                longest_occ = 1
            elif nums[i] == current_max:
                current_occ += 1
                longest_occ = max(longest_occ, current_occ)
            else:
                current_occ = 0
        return longest_occ

if __name__ == "__main__":
    inputs = [
        ([1,2,3,3,2,2], ),
        ([1,2,3,4], ),
    ]
    outputs = [
        (2),
        (1),
    ]
    x = Solution()
    evaluate(x.longestSubarray, inputs, outputs)
