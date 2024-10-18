from leetcode import evaluate

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        return self.longestDiverseStringSub(a, b, c, "")

    def longestDiverseStringSub(self, a, b, c, answer):
        if a>0 and a >= b and a >= c:
            if len(answer) < 2:
                return self.longestDiverseStringSub(a-1,b,c, answer + "a")
            elif answer[-2:] != "aa":
                return self.longestDiverseStringSub(a-1,b,c, answer + "a")
            elif b >= c and b > 0:
                return self.longestDiverseStringSub(a,b-1,c, answer + "b")
            elif c > 0:
                return self.longestDiverseStringSub(a,b,c-1, answer + "c")
            else:
                return answer
        if b>0 and b >= a and b >= c:
            if len(answer) < 2:
                return self.longestDiverseStringSub(a,b-1,c, answer + "b")
            elif answer[-2:] != "bb":
                return self.longestDiverseStringSub(a,b-1,c, answer + "b")
            elif a >= c and a > 0:
                return self.longestDiverseStringSub(a-1,b,c, answer + "a")
            elif c > 0:
                return self.longestDiverseStringSub(a,b,c-1, answer + "c")
            else:
                return answer
        if c>0 and c >= a and c >= b:
            if len(answer) < 2:
                return self.longestDiverseStringSub(a,b,c-1, answer + "c")
            elif answer[-2:] != "cc":
                return self.longestDiverseStringSub(a,b,c-1, answer + "c")
            elif a >= b and a > 0:
                return self.longestDiverseStringSub(a-1,b,c, answer + "a")
            elif b > 0:
                return self.longestDiverseStringSub(a,b-1,c, answer + "b")
            else:
                return answer
        return answer


if __name__ == "__main__":
    inputs = [
        (1, 1, 7, ),
        (7, 1, 0, ),
    ]
    outputs = [
        ("ccaccbcc"),
        ("aabaa"),
    ]
    x = Solution()
    evaluate(x.longestDiverseString, inputs, outputs)
