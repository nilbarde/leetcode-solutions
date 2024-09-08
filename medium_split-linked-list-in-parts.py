from leetcode import evaluate

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getAnswer(self, nums, k):
        if not nums:
            return [[]] * k
        head = ListNode(nums[0])
        now = head
        for n in nums[1:]:
            now.next = ListNode(n)
            now = now.next

        answer = self.splitListToParts(head, k)

        answer_simplified = []
        for l in answer:
            a = []
            while l:
                a.append(l.val)
                l = l.next
            answer_simplified.append(a)
        return answer_simplified            

    def splitListToParts(self, head, k: int):
        l = self.getLength(head)
        main_length = l // k
        extra_length_for = l % k

        answer = []
        for i in range(extra_length_for):
            answer.append(head)
            for _ in range(main_length):
                head = head.next
            head.next, head = None, head.next

        for i in range(k - extra_length_for):
            if head:
                answer.append(head)
            else:
                answer.append(None)
                continue
            for _ in range(main_length - 1):
                head = head.next
            head.next, head = None, head.next

        return answer

    def getLength(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l



if __name__ == "__main__":
    inputs = [
        ([1,2,3], 5),
        ([1,2,3,4,5,6,7,8,9,10], 3),
    ]
    outputs = [
        ([[1],[2],[3],[],[]]),
        ([[1,2,3,4],[5,6,7],[8,9,10]]),
    ]
    x = Solution()
    evaluate(x.getAnswer, inputs, outputs)
