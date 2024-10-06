from leetcode import evaluate

class Node:
    def __init__(self, freq, key):
        self.freq = freq
        self.next = None
        self.prev = None
        self.keys = set([key])


class AllOne:

    def __init__(self):
        self.head = Node(0, "")
        self.tail = Node(0, "")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2node = {}

    def attach(self, n1, n2):
        n1.next, n2.prev = n2, n1

    def inc(self, key: str) -> None:
        if key not in self.key2node:
            node = self.head
            freq = 1
        else:
            node = self.key2node[key]
            freq = node.freq + 1

            node.keys.remove(key)
            if not node.keys:
                self.attach(node.prev, node.next)
                node = node.prev

        if node.next.freq == freq:
            node.next.keys.add(key)
            self.key2node[key] = node.next
        else:
            newNode = Node(freq, key)
            self.key2node[key] = newNode
            nextNode = node.next
            self.attach(node, newNode)
            self.attach(newNode, nextNode)

    def dec(self, key: str) -> None:
        node = self.key2node[key]
        freq = node.freq - 1

        node.keys.remove(key)
        if not node.keys:
            self.attach(node.prev, node.next)
            node = node.next

        if node.prev.freq == freq:
            node.prev.keys.add(key)
            self.key2node[key] = node.prev
        else:
            newNode = Node(freq, key)
            self.key2node[key] = newNode
            prevNode = node.prev
            self.attach(newNode, node)
            self.attach(prevNode, newNode)

    def getMaxKey(self) -> str:
        if self.tail.prev.freq == 0:
            return ""
        for key in self.tail.prev.keys:
            return key

    def getMinKey(self) -> str:
        if self.head.next.freq == 0:
            return ""
        for key in self.head.next.keys:
            return key

class Solution:
    def __init__(self):
        self.ao = AllOne()

    def function(self, command, value: int) -> int:
        print(command, value)
        if command == "AllOne":
            self.ao = AllOne()
            return None
        elif command == "inc":
            self.ao.inc(value[0])
            return None
        elif command == "dec":
            self.ao.dec(value[0])
            return None
        elif command == "getMaxKey":
            return self.ao.getMaxKey()
        elif command == "getMinKey":
            return self.ao.getMinKey()
        else:
            raise Exception(f"wrong command")


if __name__ == "__main__":
    inputs = [
        ["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"], [[],["hello"],["hello"],[],[],["leet"],[],[]],
    ]
    inputs = [(x, y) for x,y in zip(inputs[0], inputs[1])]
    outputs = [
        None, None, None, "hello", "hello", None, "hello", "leet",
    ]
    x = Solution()
    evaluate(x.function, inputs, outputs)
