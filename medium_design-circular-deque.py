from leetcode import evaluate

class MyCircularDeque:

    def __init__(self, k: int):
        self.array = []
        self.maxSize = k
        self.currentSize = 0

    def insertFront(self, value: int) -> bool:
        if self.currentSize >= self.maxSize:
            return False

        self.array.append(value)
        self.currentSize += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.currentSize >= self.maxSize:
            return False

        self.array.insert(0, value)
        self.currentSize += 1

        return True

    def deleteFront(self) -> bool:
        if self.currentSize == 0:
            return False

        self.array.pop()
        self.currentSize -= 1

        return True

    def deleteLast(self) -> bool:
        if self.currentSize == 0:
            return False

        self.array.pop(0)
        self.currentSize -= 1

        return True

    def getFront(self) -> int:
        if self.currentSize == 0:
            return -1

        return self.array[-1]

    def getRear(self) -> int:
        if self.currentSize == 0:
            return -1

        return self.array[0]

    def isEmpty(self) -> bool:
        return self.currentSize == 0

    def isFull(self) -> bool:
        return self.currentSize == self.maxSize
        


if __name__ == "__main__":
    inputs = [
        (123, ),
    ]
    outputs = [
        (123),
    ]
    x = Solution()
    evaluate(x.function, inputs, outputs)
