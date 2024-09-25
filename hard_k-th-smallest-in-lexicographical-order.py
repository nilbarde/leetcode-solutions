from leetcode import evaluate

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        num = 1
        current_i = 1
        while current_i < k:
            gap = self.getGap(num, num+1, n)
            if current_i + gap <= k:
                current_i += gap
                num += 1
            else:
                current_i += 1
                num *= 10
        return num

    def getGap(self, lower, higher, n):
        gap = 0
        while lower <= n:
            gap += min(n + 1, higher) - lower
            lower *= 10
            higher *= 10
        return gap
    
    def findKthNumber2(self, n: int, k: int) -> int:
        # print(len(str(n)))
        digits = len(str(n))
        each_i = int(digits * "1")
        digit1 = ((k - 1) // each_i) + 1
        print(each_i, digit1)
        answer = str(digit1)
        answer += self.findKthNumberInner(k - ((each_i) * (digit1 - 1)))

        return 0

    def findKthNumberInner(self, n: int, k: int) -> int:
        pass

    def findKthNumberOld(self, n: int, k: int) -> int:
        num = 1
        # answer = []
        self.answer = 0
        self.current_k = 0
        self.required_k = k

        for i in range(9):
            num_now = num + i
            if num_now <= n:
                self.current_k += 1
                if self.current_k == self.required_k:
                    self.answer = num_now
                    print("1", self.current_k)
                    return num_now
                # answer.append(num_now)
                next_num = (num_now) * 10
                a = self.getList(next_num, n)
                if a != 0:
                    print("2", a)
                    return a
            else:
                break
        return self.answer

    def getList(self, num, n):
        # answer = []
        for i in range(10):
            num_now = num + i
            if num_now <= n:
                self.current_k += 1
                # print(self.current_k, self.required_k)
                if self.current_k == self.required_k:
                    print("1", self.current_k)
                    self.answer = num_now
                    return num_now
                # answer.append(num_now)
                next_num = (num_now) * 10
                return self.getList(next_num, n)
            else:
                break
        return 0


if __name__ == "__main__":
    inputs = [
        (13, 2, ),
        (1, 1, ),
        (120, 6, )
        # (5180541, 1762750, )
    ]
    outputs = [
        (10),
        (1),
        (103),
        # (2586472),
    ]
    x = Solution()
    evaluate(x.findKthNumber, inputs, outputs, debug=False)
