from leetcode import evaluate


class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack):
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


class Solution:
    def function(self, x: int) -> int:
        return x


if __name__ == "__main__":
    inputs = [
        (123, ),
    ]
    outputs = [
        (123),
    ]
    x = Solution()
    evaluate(x.function, inputs, outputs)
