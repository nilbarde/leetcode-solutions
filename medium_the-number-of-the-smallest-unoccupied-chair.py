from leetcode import evaluate

class Solution:
    def smallestChair(self, times, targetFriend) -> int:
        timeTarget = times[targetFriend][0]
        actions = []
        for numFriend, timeDetails in enumerate(times):
            timeStart = timeDetails[0]
            timeEnd = timeDetails[1]

            if timeStart <= timeTarget:
                actions.append((timeStart, 1, numFriend))
                if timeEnd <= timeTarget:
                    actions.append((timeEnd, 0, numFriend))
        actions.sort()
        # print(actions)

        occupied = set()
        availableLeast = 0
        person2chair = {}
        for action in actions:
            # print(action)
            if action[1] == 1:
                person2chair[action[2]] = availableLeast
                occupied.add(availableLeast)
                while availableLeast in occupied:
                    availableLeast += 1
            else:
                chairNum = person2chair[action[2]]
                del person2chair[action[2]]
                occupied.remove(chairNum)
                if availableLeast > chairNum:
                    availableLeast = chairNum

        return person2chair[targetFriend]


if __name__ == "__main__":
    inputs = [
        ([[1,4],[2,3],[4,6]], 1, ),
        ([[3,10],[1,5],[2,6]], 0, ),
        ([[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]], 6)
    ]
    outputs = [
        (1),
        (2),
        (2),
    ]
    x = Solution()
    evaluate(x.smallestChair, inputs, outputs)
