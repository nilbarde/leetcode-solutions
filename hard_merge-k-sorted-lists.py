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

def makeList(linkedList):
    l = []
    while linkedList:
        l.append(linkedList.val)
        linkedList = linkedList.next
    return l

class Solution:
    def getAnswer(self, lists):
        lists = [makeLinkedList(l) for l in lists]
        answer = self.mergeKLists(lists)
        return makeList(answer)

    def mergeKLists(self, lists):
        heads = [l for l in lists if l]
        answer = ListNode()
        now = answer
        while heads:
            min_head = heads[0]
            min_index = 0
            for i, head in enumerate(heads):
                if head.val < min_head.val:
                    min_head = head
                    min_index = i
            now.next = min_head
            now = now.next
            heads[min_index] = heads[min_index].next
            if not heads[min_index]:
                heads.pop(min_index)
        return answer.next

if __name__ == "__main__":
    inputs = [
        ([[1,4,5],[1,3,4],[2,6]], ),
        ([], ),
    ]
    outputs = [
        ([1,1,2,3,4,4,5,6]),
        ([]),
    ]
    x = Solution()
    evaluate(x.getAnswer, inputs, outputs)
