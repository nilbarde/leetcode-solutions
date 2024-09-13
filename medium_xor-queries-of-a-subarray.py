from leetcode import evaluate
from tqdm import tqdm

import bisect

class Solution:
    def xorQueries(self, arr, queries):
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] ^ arr[i])
        # print(prefix)
        result = []
        for query in queries:
            if query[0] == 0:
                result.append(prefix[query[1]])
            else:
                result.append(prefix[query[0] - 1] ^ prefix[query[1]])
        return result


if __name__ == "__main__":
    import json
    data = json.load(open("testcases/xor-queries-of-a-subarray.json"))

    # inputs = [
    #     ([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]], ),
    #     ([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]], ),
    # ]
    # outputs = [
    #     ([2,7,14,8]),
    #     ([8,0,4,4])
    # ]

    x = Solution()
    evaluate(x.xorQueries, data["inputs"], data["outputs"])
