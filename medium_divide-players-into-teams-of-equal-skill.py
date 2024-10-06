from leetcode import evaluate
from collections import defaultdict

class Solution:
    def dividePlayers(self, skill) -> int:
        counts = defaultdict(int)
        total = 0
        for s in skill:
            counts[s] += 1
            total += s

        chemistry = 0
        sum_req = total * 2 / len(skill)

        for num in counts:
            num2 = sum_req - num
            if num == num2:
                if counts[num] % 2 != 0:
                    return -1
                # chemistry += num*num2*counts[num] / 2
            else:
                if counts[num] != counts[num2]:
                    return -1                    
            chemistry += num*num2*counts[num] / 2


        return int(chemistry)


if __name__ == "__main__":
    inputs = [
        ([3,2,5,1,3,4], ),
        ([3,4], ),
        ([1,1,2,3], ),
        ([4,4,2,6], )
    ]
    outputs = [
        (22),
        (12),
        (-1),
        (28),
    ]
    x = Solution()
    evaluate(x.dividePlayers, inputs, outputs)
