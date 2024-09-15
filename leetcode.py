import time

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

def evaluate(function, inputs, outputs, evaluate_time=False, debug=False):
    for input_num, (i, o) in enumerate(zip(inputs, outputs)):
        a = time.time()
        if evaluate_time:
            for _ in range(100):
                function_output = function(*i)
        else:
            function_output = function(*i)
        b = time.time()
        if o == function_output:
            print(f"input {input_num} solved correctly in {b-a}sec")
        elif not debug:
            raise Exception(f"Output not matched \n\
    input: {i}\n\
    output expected : {o}\n\
    output generated: {function_output}\n")
    print(f"{len(inputs)} solved correctly")
    return True
