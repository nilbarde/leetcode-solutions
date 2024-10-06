from leetcode import evaluate
from collections import defaultdict

class Solution:
    def canArrange(self, arr, k: int) -> bool:
        reminder_counts = defaultdict(int)
        for a in arr:
            reminder_counts[a%k] += 1

        for r, v in reminder_counts.items():
            if r == 0:
                if v%2:
                    return False
                continue
            if reminder_counts[r] != reminder_counts[k - r]:
                return False
        return True

if __name__ == "__main__":
    inputs = [
        ([1,2,3,4,5,10,6,7,8,9],  5, ),
        ([1,2,3,4,5,6], 7, ),
        ([1,2,3,4,5,6], 10, ),
    ]
    outputs = [
        (True),
        (True),
        (False),
    ]
    x = Solution()
    evaluate(x.canArrange, inputs, outputs)
