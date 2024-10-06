from leetcode import evaluate

class Solution:
    def arrayRankTransform(self, arr):
        if not arr:
            return []
        arr = [(a, i) for i, a in enumerate(arr)]
        arr.sort()
        # print(arr)
        ranks = [-1] * len(arr)
        prev_rank = 2
        ranks[arr[0][1]] = 1
        for i in range(1, len(arr)):
            # print(arr[i])
            if arr[i][0] == arr[i-1][0]:
                prev_rank -= 1
                ranks[arr[i][1]] = prev_rank
                prev_rank += 1
            else:
                ranks[arr[i][1]] = prev_rank
                prev_rank += 1
            # print(ranks)
        return ranks


if __name__ == "__main__":
    inputs = [
        ([40,10,20,30], ),
        ([100,100,100], ),
        ([37,12,28,9,100,56,80,5,12], )
    ]
    outputs = [
        ([4,1,2,3]),
        ([1,1,1]),
        ([5,3,4,2,8,6,7,1,3]),
    ]
    x = Solution()
    evaluate(x.arrayRankTransform, inputs, outputs)
