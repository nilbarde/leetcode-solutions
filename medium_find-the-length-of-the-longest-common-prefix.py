from leetcode import evaluate

def Node():
    def __init__(self, val):
        self.value = val
        self.leaves = []

    def add_leaf(self, leaf: Node):
        self.leaves.append(leaf)

class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        arr1 = [str(a) for a in arr1]
        arr2 = [str(a) for a in arr2]
        arr1.sort()
        arr2.sort()
        answer = 0

        i1, i2 = 0, 0
        while i1 < len(arr1) and i2 < len(arr2):
            if len(arr1[i1]) > answer and len(arr2[i2]) > answer and arr1[i1][:answer] == arr2[i2][:answer]:
                answer = max(answer, self.getPrefixLength(arr1[i1], arr2[i2], answer))
            if arr1[i1] > arr2[i2]:
                i2 += 1
            elif arr1[i1] < arr2[i2]:
                i1 += 1
            else:
                i1 += 1
                i2 += 1
        return answer

    def longestCommonPrefix2(self, arr1, arr2) -> int:
        arr1 = [str(a) for a in arr1]
        arr2 = [str(a) for a in arr2]

        answer = 0
        for a1 in arr1:
            if len(a1) < answer:
                continue
            for a2 in arr2:
                if len(a2) < answer:
                    continue
                if a1[:answer] == a2[:answer]:
                    answer = max(answer, self.getPrefixLength(a1, a2, answer))
        return answer

    def getPrefixLength(self, a1, a2, skips):
        prefix = skips
        for aa1, aa2 in zip(a1[skips:], a2[skips:]):
            if aa1 == aa2:
                prefix += 1
            else:
                break
            
        return prefix


if __name__ == "__main__":
    import json
    data = json.load(open("testcases/medium_find-the-length-of-the-longest-common-prefix.json"))
    inputs, outputs = data["inputs"], data["outputs"]

    x = Solution()
    evaluate(x.longestCommonPrefix, inputs, outputs)
