# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeLinkedList(numbers):
    origin = ListNode(numbers[0])
    last = origin
    for i in range(1, len(numbers)):
        node = ListNode(numbers[i])
        last.next = node
        last = node
    return origin

def makeList(origin):
    numbers = []
    node = origin
    while node:
        numbers.append(node.val)
        node = node.next
    return numbers
