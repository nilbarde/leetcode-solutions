from leetcode import evaluate


class MyCalendar:

    def __init__(self):
        self.bookings = []
        

    def book(self, start: int, end: int) -> bool:
        if len(self.bookings) == 0:
            self.bookings.append([start, end])
            return True
        else:
            if end <= self.bookings[0][0]:
                self.bookings.insert(0, [start, end])
                return True
            for i in range(1, len(self.bookings)):
                if start < self.bookings[i-1][1]:
                    return False
                elif start <= self.bookings[i][0]:
                    if end <= self.bookings[i][0]:
                        self.bookings.insert(i, [start, end])
                        return True
                    else:
                        return False
            if start >= self.bookings[-1][1]:
                self.bookings.append([start, end])
                return True
                

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
