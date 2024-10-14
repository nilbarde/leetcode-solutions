from leetcode import evaluate
import math
import heapq

class Solution:
    def maxKelements(self, nums, k: int) -> int:
        score = 0
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k):
            score_now = -heapq.heappop(heap)
            score += score_now
            heapq.heappush(heap, -math.ceil(score_now / 3))

        return score


if __name__ == "__main__":
    inputs = [
        ([10,10,10,10,10], 5),
        ([1,10,3,3,3], 3),
        ([564960737], 1)
    ]
    outputs = [
        (50),
        (17),
        (564960737),
    ]
    x = Solution()
    evaluate(x.maxKelements, inputs, outputs)
