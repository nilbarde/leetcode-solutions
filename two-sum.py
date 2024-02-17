# link -> https://leetcode.com/problems/two-sum/description/

from leetcode import evaluate

class Solution:
    def twoSum(self, nums, target):
        
        numsTupled = [(n, i) for i, n in enumerate(nums)]
        numsTupled.sort()
        i, j = 0, len(nums) -1
        just_started = False
        while True:
            print(i, j)
            sum_now = numsTupled[i][0] + numsTupled[j][0]
            if sum_now == target:
                return [numsTupled[i][1], numsTupled[j][1]]
            elif sum_now > target:
                j -= 1
                just_started = False
            elif sum_now < target:
                if (not just_started) or (j==len(nums)-1):
                    i += 1
                    just_started = True
                else:
                    j += 1

if __name__ == "__main__":
    print("solving")
    inputs = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 6142, 8192, 10239], 18431),
    ]
    outputs = [
        ([0, 1]),
        ([1, 2]),
        ([0, 1]),
        ([2, 3]),
    ]
    x = Solution()
    evaluate(x.twoSum, inputs, outputs)
