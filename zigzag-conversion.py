# link -> https://leetcode.com/problems/zigzag-conversion/

from leetcode import evaluate

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        charInPattern = numRows * 2 - 2
        completePattern = int(len(s) // charInPattern)
        answer = s[::charInPattern]
        # print(charInPattern, completePattern)
        # print(answer)
        for i in range(1, numRows-1):
            for n in range(completePattern):
                # print(charInPattern * n + i, charInPattern * (n + 1) - i)
                answer += s[charInPattern * n + i]
                answer += s[charInPattern * (n + 1) - i]
            # print(answer)
            n = completePattern
            j = charInPattern * n + i
            if j < len(s):
                answer += s[j]
                j = charInPattern * (n + 1) - i
                if j < len(s):
                    answer += s[j]
            # print(answer)

        answer += s[numRows - 1::charInPattern]
        # print(answer)
        return answer

if __name__ == "__main__":
    inputs = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
    ]
    outputs = [
        ("PAHNAPLSIIGYIR"),
        ("PINALSIGYAHRPI"),
        ("A"),
    ]
    x = Solution()
    evaluate(x.convert, inputs, outputs)
