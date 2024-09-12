from leetcode import evaluate

class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        allowed = set(allowed)
        answer = len(words)
        for word in words:
            word_set = set(word)
            for w in word_set:
                if not w in allowed:
                    answer -= 1
                    break
        return answer

    def countConsistentStrings2(self, allowed: str, words) -> int:
        allowed = set(allowed)
        answer = 0
        for word in words:
            word_set = set(word)
            if not word_set - allowed:
                answer += 1
        return answer

if __name__ == "__main__":
    inputs = [
        ("ab", ["ad","bd","aaab","baa","badab"]),
        ("abc", ["a","b","c","ab","ac","bc","abc"]),
        ("cad", ["cc","acd","b","ba","bac","bad","ac","d"]),
    ]
    outputs = [
        (2),
        (7),
        (4),
    ]
    x = Solution()
    evaluate(x.countConsistentStrings, inputs, outputs)
