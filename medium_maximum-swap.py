from leetcode import evaluate

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        values = [(9-int(x), i) for i, x in enumerate(num_str)]
        values = sorted(values)
        for i in range(len(values)):
            if i != values[i][1]:
                replace_index1 = i
                replace_ref = i #values[i][1]
                while replace_ref < len(num_str) and values[replace_ref][0] == values[replace_ref+1][0]:
                    replace_ref += 1
                replace_index2 = values[replace_ref][1]

                return int(num_str[:replace_index1] + num_str[replace_index2] + num_str[replace_index1+1:replace_index2] + num_str[replace_index1] + num_str[replace_index2+1:])
        return num


if __name__ == "__main__":
    inputs = [
        (2736, ),
        (9973, ),
        (98368, ),
        (1993, ),
    ]
    outputs = [
        (7236),
        (9973),
        (98863),
        (9913),
    ]
    x = Solution()
    evaluate(x.maximumSwap, inputs, outputs)
