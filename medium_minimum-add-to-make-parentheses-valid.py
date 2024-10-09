from leetcode import evaluate

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        curr_count = 0
        answer = 0
        for ss in s:
            if ss == "(":
                curr_count += 1
            else:
                if curr_count:
                    curr_count -= 1
                else:
                    answer += 1
        answer += curr_count
        return answer


if __name__ == "__main__":
    inputs = [
        ("())", ),
        ("(((", ),
    ]
    outputs = [
        (1),
        (3),
    ]
    x = Solution()
    evaluate(x.minAddToMakeValid, inputs, outputs)
