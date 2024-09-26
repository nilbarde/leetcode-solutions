from leetcode import evaluate

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.value = 0
        self.leaves = {}

    def get_leaf(self, name):
        if name not in self.leaves:
            leaf = Node(name)
            self.leaves[name] = leaf
        return self.leaves[name]

    def display_tree(self, level):
        print("--"*level + " " + self.name + " " + str(self.value))
        for leaf in self.leaves.values():
            leaf.display_tree(level + 1)

class Solution:
    def sumPrefixScores(self, words):
        root = Node("")
        for word in words:
            # print(word)
            now = root
            for char in word:
                next = now.get_leaf(char)
                next.value += 1
                now = next
            # root.display_tree(0)
            # print("...........")

        answer = []
        for word in words:
            now = root
            now_val = 0
            for char in word:
                next = now.get_leaf(char)
                now_val += next.value
                now = next
            answer.append(now_val)
        return answer


if __name__ == "__main__":
    inputs = [
        (["abc","ab","bc","b"], ),
        (["abcd"], ),
    ]
    outputs = [
        ([5,4,3,2]),
        ([4]),
    ]
    x = Solution()
    evaluate(x.sumPrefixScores, inputs, outputs)
