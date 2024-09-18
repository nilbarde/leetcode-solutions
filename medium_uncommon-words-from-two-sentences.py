from leetcode import evaluate
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        words1 = Counter(s1.split(" "))
        words2 = Counter(s2.split(" "))

        answer = []
        for word in words1:
            if words1[word] == 1 and word not in words2:
                answer.append(word)
        for word in words2:
            if words2[word] == 1 and word not in words1:
                answer.append(word)
        return answer


if __name__ == "__main__":
    inputs = [
        ("this apple is sweet", "this apple is sour"),
        ("apple apple", "banana"),
    ]
    outputs = [
        (["sweet","sour"]),
        (["banana"])
    ]
    x = Solution()
    evaluate(x.uncommonFromSentences, inputs, outputs)
