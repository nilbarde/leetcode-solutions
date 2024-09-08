from leetcode import evaluate

def get_index(current_list, value):
    curr_len = len(current_list)
    if curr_len == 0:
        return 0
    elif curr_len == 1:
        if value < current_list[0]:
            return -1
        return 0
    else:
        if value < current_list[0]:
            return -1
        if value >= current_list[-1]:
            return curr_len - 1
        l_index, h_index = 0, curr_len - 1
        curr_index = int((l_index + h_index) / 2)
        while not(current_list[curr_index] <= value < current_list[curr_index+1]):
            if value < current_list[curr_index]:
                h_index = curr_index
            else:
                l_index = curr_index
            curr_index = int((l_index + h_index) / 2)
        return curr_index


class TimeMap:

    def __init__(self):
        self._memory = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._memory:
            self._memory[key] = [[], []]
        self._memory[key][0].append(timestamp)
        self._memory[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._memory:
            return ""
        index = get_index(self._memory[key][0], timestamp)
        if index == -1:
            return ""
        else:
            return self._memory[key][1][index]        

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
