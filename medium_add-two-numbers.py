# link -> https://leetcode.com/problems/add-two-numbers/

from leetcode import evaluate

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeListNode(numbers):
    origin = ListNode(numbers[0])
    last = origin
    for i in range(1, len(numbers)):
        node = ListNode(numbers[i])
        last.next = node
        last = node
    return origin

def unwrapListNode(origin):
    numbers = []
    node = origin
    while node:
        numbers.append(node.val)
        node = node.next
    return numbers

class Solution:
    def addTwoNumbers(self, l1, l2):
        head_l1 = l1

        now = l1.val + l2.val
        carry_over, now = int(now / 10), now % 10
        l1.val, l2.val = now, now

        while l1.next or l2.next or carry_over:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            l1, l2 = l1.next, l2.next
            now = l1.val + l2.val + carry_over
            carry_over, now = int(now / 10), now % 10
            l1.val, l2.val = now, now
        return head_l1

    def addTwoNumbersProcessor(self, nums1, nums2):
        return unwrapListNode(self.addTwoNumbers(makeListNode(nums1), makeListNode(nums2)))

if __name__ == "__main__":
    inputs = [
        ([2,4,3], [5,6,4]),
        ([5,6,4], [2,4,3]),
        ([0], [0]),
        ([9,9,9,9,9,9,9], [9,9,9,9]),
        ([9,9,9,9], [9,9,9,9,9,9,9]),
        ([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [5,6,4])
    ]
    outputs = [
        ([7,0,8]),
        ([7,0,8]),
        ([0]),
        ([8,9,9,9,0,0,0,1]),
        ([8,9,9,9,0,0,0,1]),
        ([6,6,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    ]
    x = Solution()
    evaluate(x.addTwoNumbersProcessor, inputs, outputs)
 