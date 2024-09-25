from leetcode import evaluate
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        counts = []
        count_now = defaultdict(int)
        found = False
        last_start = -1
        last_start_count_index = 0
        answer = len(s) + 1
        answer_start, answer_end = -1, -1
        for i, ss in enumerate(s):
            if ss in t_counts:
                count_now[ss] += 1
                counts.append([i, count_now.copy()])
                found_now = True
                for req_letter, req_freq in t_counts.items():
                    print(f"Checking frequency for {req_letter}, need {req_freq}, have {count_now[req_letter]}, result {not (req_freq >= count_now[req_letter])}")
                    if not (req_freq <= count_now[req_letter]):
                        found_now = False
                        break
                print("1-", i, found_now)
                if found_now:
                    if not found:
                        answer = i - counts[0][0] + 1
                        answer_start, answer_end = counts[0][0], i
                    found = True
                    for j in range(last_start_count_index, len(counts) - 1):
                        found_case = True
                        for req_letter, req_freq in t_counts.items():
                            if not (count_now[req_letter] - counts[j][1][req_letter] >= req_freq):
                                found_case = False
                                break
                        if not found_case:
                            break
                        else:
                            last_start_count_index = j
                            answer_now = i - counts[j][0] + 1
                            if answer_now < answer:
                                answer = answer_now
                                answer_start = counts[j][0]
                                answer_end = i
                print(i, answer)
        print(counts)
        return s[answer_start: answer_end+1]


if __name__ == "__main__":
    inputs = [
        ("ADOBECODEBANC", "ABC", ),
        ("a", "a", ),
        ("a", "aa", ),
    ]
    outputs = [
        ("BANC"),
        ("a"),
        (""),
    ]
    x = Solution()
    evaluate(x.minWindow, inputs, outputs, debug=False)
