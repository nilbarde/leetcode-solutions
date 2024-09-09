from leetcode import evaluate

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeLinkedList(nums):
    head = ListNode(nums[0])
    now = head
    for n in nums[1:]:
        now.next = ListNode(n)
        now = now.next
    return head

class Solution:
    def getAnswer(self, m: int, n: int, array) -> int:
        return self.spiralMatrix(m, n, makeLinkedList(array))

    def spiralMatrix(self, m: int, n: int, head):
        matrix = [[-1 for nn in range(n)] for mm in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        i, j = 0, 0
        while head:
            matrix[i][j] = head.val
            head = head.next
            i_next, j_next = i + directions[current_direction][0], j + directions[current_direction][1]
            if not (0 <= i_next < m and 0 <= j_next < n and matrix[i_next][j_next] == -1):
                current_direction = (current_direction + 1) % 4
            i_next, j_next = i + directions[current_direction][0], j + directions[current_direction][1]
            i, j = i_next, j_next
        return matrix

if __name__ == "__main__":
    inputs = [
        (3, 5, [3,0,2,6,8,1,7,9,4,2,5,5,0], ),
        (1, 4, [0,1,2], )
    ]
    outputs = [
        ([[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]),
        ([[0,1,2,-1]]),
    ]
    x = Solution()
    evaluate(x.getAnswer, inputs, outputs)
