from leetcode import evaluate, ListNode, makeLinkedList, makeList

class Solution:
    def getAnswer(self, lists):
        linkedList = makeLinkedList(lists)
        answer = self.insertGreatestCommonDivisors(linkedList)
        return makeList(answer)

    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        root = head
        while head.next:
            if head.val > head.next.val:
                gcd = self.gcd(head.val, head.next.val)
            else:
                gcd = self.gcd(head.next.val, head.val)
            head.next = ListNode(gcd, head.next)
            head = head.next.next
        return root

    def gcd(self, a, b):
        if a%b == 0:
            return b
        else:
            return self.gcd(b, a%b)


if __name__ == "__main__":
    inputs = [
        ([18,6,10,3], ),
        ([7], ),
    ]
    outputs = [
        ([18,6,6,2,10,1,3]),
        ([7]),
    ]
    x = Solution()
    evaluate(x.getAnswer, inputs, outputs)
