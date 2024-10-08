# link -> https://leetcode.com/problems/sample/

from leetcode import evaluate
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mCount = Counter(magazine)
        for r in ransomNote:
            if not r in mCount:
                return False
            mCount[r] -= 1
            if mCount[r] < 0:
                return False
        return True

    def canConstructV1(self, ransomNote: str, magazine: str) -> bool:
        rCount = Counter(ransomNote)
        mCount = Counter(magazine)
        for letter, req in rCount.items():
            if not letter in mCount:
                return False
            if mCount[letter] < rCount[letter]:
                return False
        return True

if __name__ == "__main__":
    inputs = [
        ("a", "b"),
        ("aa", "ab"),
        ("aa", "aab"),
        ("aab", "baa"),
    ]
    outputs = [
        (False),
        (False),
        (True),
        (True),
    ]
    x = Solution()
    evaluate(x.canConstruct, inputs, outputs)
