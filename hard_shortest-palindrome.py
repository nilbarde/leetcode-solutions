from leetcode import evaluate

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        first_letter = s[0]
        for i in range(len(s)-1, 0, -1):
            if s[i] == first_letter:
                if self.isPalindrome(s[1:i]):
                    return s[:i:-1] + s
        return s[:0:-1] + s

    def isPalindrome(self, s):
        l = len(s) // 2
        r = len(s) - l - 1
        return s[:l] == s[:r:-1]

if __name__ == "__main__":
    inputs = [
        ("aacecaaa", ),
        ("abcd", ),
        ("abbacd", )
    ]
    outputs = [
        ("aaacecaaa"),
        ("dcbabcd"),
        ("dcabbacd")
    ]
    x = Solution()
    evaluate(x.shortestPalindrome, inputs, outputs)
