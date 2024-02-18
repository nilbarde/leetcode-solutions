# link -> https://leetcode.com/problems/longest-substring-without-repeating-characters/
from leetcode import evaluate

class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        prev_occur_store = {}
        prev_occur = [-1] * len(s)
        for i in range(len(s)):
            c = s[i]
            if c in prev_occur_store:
                prev_occur[i] = prev_occur_store[c]
            prev_occur_store[c] = i

        ans = 1
        for i in range(len(s)-1):
            found = False
            for j in range(i+1, len(s)):
               if prev_occur[j] != -1 and prev_occur[j] >= i:
                    ans = max(ans, j - i)
                    found = True
                    break
            if not found:
                    ans = max(ans, len(s) - i)                
        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        prev_occur_store = {}
        prev_occur = [-1] * len(s)
        for i in range(len(s)):
            c = s[i]
            if c in prev_occur_store:
                prev_occur[i] = prev_occur_store[c]
            prev_occur_store[c] = i
        del prev_occur_store
        ans = 1
        longest = [-1]
        for i in range(1, len(s)):
            longest.append(max(longest[-1], prev_occur[i]))
            ans = max(ans, i - longest[-1])
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        prev_occur_store = {s[0]: 0}
        ans = 1
        longest = -1
        for i in range(1, len(s)):
            prev_occur = prev_occur_store[s[i]] if s[i] in prev_occur_store else -1
            prev_occur_store[s[i]] = i
            longest = max(longest, prev_occur)
            ans = max(ans, i - longest)
        return ans


if __name__ == "__main__":
    inputs = [
        ("abcabcbb", ),
        ("bbbb", ),
        ("pwwkew", ),
    ]
    outputs = [
        (3),
        (1),
        (3),
    ]
    x = Solution()
    evaluate(x.lengthOfLongestSubstring, inputs, outputs)
