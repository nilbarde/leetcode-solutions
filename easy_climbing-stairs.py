from leetcode import evaluate

"""
9
4 1


"""


class Solution:
    def climbStairs(self, n: int) -> int:
        num_1 = n%2
        num_2 = n//2
        num = num_1 + num_2
        methods = 0

        if num_1 == 0:
            nume_mul_high = num_2 + 1
            nume_mul_low = num_2
            nume = 1
            deno = 1
            methods += 1
        else:
            nume_mul_high = num + 1
            nume_mul_low = num - 1
            nume = num_2 + 1
            deno = 1
            methods += num

        while num_1 <= n:
            nume *= nume_mul_high * nume_mul_low
            deno *= (num_1 + 1) * (num_1 + 2)
            methods += nume / deno
            nume_mul_high += 1
            nume_mul_low -= 1
            num_1 += 2
            num_2 -= 1

        return int(methods)

if __name__ == "__main__":
    inputs = [
        (2, ),
        (3, ),
    ]
    outputs = [
        (2),
        (3),
    ]
    x = Solution()
    evaluate(x.climbStairs, inputs, outputs)
