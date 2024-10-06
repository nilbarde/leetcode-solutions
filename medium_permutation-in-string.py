from leetcode import evaluate

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        length_to_find = len(s1)
        chars_to_find = defaultdict(int)
        for s in s1:
            chars_to_find[s] += 1

        chars_now = defaultdict(int)
        for i in range(length_to_find):
            chars_now[s2[i]] += 1

        if self.isPermutation(chars_to_find, chars_now):
            return True

        for i in range(1, len(s2) - length_to_find + 1):
            chars_now[s2[i-1]] -= 1
            chars_now[s2[i-1+length_to_find]] += 1
            if self.isPermutation(chars_to_find, chars_now):
                return True

        return False

    def isPermutation(self, count_s1, count_s2):
        for s, v in count_s1.items():
            if count_s1[s] != count_s2[s]:
                return False
        return True

if __name__ == "__main__":
    inputs = [
        ("ab", "eidbaooo"),
        ("ab", "eidboaooo"),
    ]
    outputs = [
        (True),
        (False),
    ]
    x = Solution()
    evaluate(x.checkInclusion, inputs, outputs)
