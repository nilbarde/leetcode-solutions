from leetcode import evaluate
from collections import defaultdict

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        char_map = defaultdict(int)
        char_map["a"] = 1
        char_map["e"] = 2
        char_map["i"] = 4
        char_map["o"] = 8
        char_map["u"] = 16
        char_map[""] = 0
        xor_list = [0]
        xor = 0
        for ss in s:
            xor ^= char_map[ss]
            xor_list.append(xor)
        first_last = {}
        for i, x in enumerate(xor_list):
            if x not in first_last:
                first_last[x] = [-1, -1]
            if first_last[x][0] == -1:
                first_last[x][0] = i
            first_last[x][1] = i
        max_len = 0
        for x in first_last:
            if first_last[x][0] != -1:
                max_len = max(max_len, first_last[x][1] - first_last[x][0])
        return max_len

if __name__ == "__main__":
    inputs = [
        ("eleetminicoworoep", ),
        ("leetcodeisgreat", ),
        ("bcbcbc", ),
    ]
    outputs = [
        (13),
        (5),
        (6),
    ]
    x = Solution()
    evaluate(x.findTheLongestSubstring, inputs, outputs, debug=False)
