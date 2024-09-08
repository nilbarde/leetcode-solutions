# link -> https://leetcode.com/problems/longest-palindromic-substring/

from leetcode import evaluate

class Solution:
    def checkOddPalindrome(self, s, center, iter_for):
        for i in range(1, iter_for + 1):
            if s[center - i] != s[center + i]:
                return 2 * i - 1, s[center - i + 1: center + i]
        return 2 * iter_for + 1, s[center - iter_for: center + iter_for + 1]

    def checkEvenPalindrome(self, s, center, iter_for):
        for i in range(iter_for):
            if s[center - i] != s[center + 1 + i]:
                return 2 * i, s[center - i + 1: center + i + 1]
        return 2 * iter_for, s[center - iter_for + 1: center + iter_for + 1]

    def longestPalindrome(self, s: str) -> str:
        # center index to check
        # len 9 -> len p odd  -> 4  3 5  2 6  1 7  
        # len 9 -> len p even -> 4  3 5  2 6  1 7  0
        # len 8 -> len p odd  ->    3 4  2 5  1 6    
        # len 8 -> len p even ->    3 4  2 5  1 6  0
        len_s = len(s)
        index_l = int((len_s - 1) / 2)
        index_r = int((len_s) / 2)

        ans, p = 1, s[0]
        if len_s % 2:
            for_loop_init = index_l - 1
            ans1, p_now = self.checkOddPalindrome(s, index_l, for_loop_init + 1)
            if ans < ans1:
                ans, p = ans1, p_now
            ans1, p_now = self.checkEvenPalindrome(s, index_l, for_loop_init + 1)
            if ans < ans1:
                ans, p = ans1, p_now
            index_l -= 1
            index_r += 1
        else:
            for_loop_init = index_l
        # # print("--")

        for i in range(for_loop_init):
            if ans < (2 * index_l + 2):
                ans1, p_now = self.checkEvenPalindrome(s, index_l, index_l + 1)
                if ans < ans1:
                    ans, p = ans1, p_now
                    # print("-", i, ans, p)
                if ans < (2 * index_l + 1):
                    ans1, p_now = self.checkOddPalindrome(s, index_l, index_l)
                    if ans < ans1:
                        ans, p = ans1, p_now
                        # print("-", i, ans, p)
                    ans1, p_now = self.checkOddPalindrome(s, index_r, index_l)
                    if ans < ans1:
                        ans, p = ans1, p_now
                        # print("-", i, ans, p)
                    if ans < (2 * index_l):
                        ans1, p_now = self.checkEvenPalindrome(s, index_r, index_l)
                        if ans < ans1:
                            ans, p = ans1, p_now
                            # print("-", i, ans, p)
            else:
                break
            index_l -= 1
            index_r += 1
            # # print(i, ans, p)

        if ans < 2:
            if len_s > 1:
                if s[0] == s[1]:
                    ans, p = 2, s[:2]
        # print(len(s), len(p))
        return p


if __name__ == "__main__":
    inputs = [
        ("assal", ),
        ("321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123", ),
        ("abb", ),
        ("ccc", ),

        ("babad", ),
        ("cbbd", ),

        ("asdfghjk", ),
        ("asdfghjkl", ),

        ("asdsghjk", ),
        ("asddshjk", ),
        ("aadfghjk", ),

        ("asddshjkl", ),
        ("asdrdshkl", ),
    ]
    outputs = [
        ("assa"),
        ("321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123"),
        ("bb"),
        ("ccc"),

        ("aba"),
        ("bb"),

        ("a"),
        ("a"),

        ("sds"),
        ("sdds"),
        ("aa"),

        ("sdds"),
        ("sdrds"),


    ]
    x = Solution()
    # print(len(outputs[0]))
    evaluate(x.longestPalindrome, inputs, outputs)
