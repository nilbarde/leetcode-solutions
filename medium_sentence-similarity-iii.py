from leetcode import evaluate

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")
        # print(words1, words2)
        if len(words1) < len(words2):
            return self.areSentencesSimilar(sentence2, sentence1)

        completed = 0
        for i in range(len(words2)):
            if words1[i] == words2[i]:
                completed += 1
            else:
                break
        # print(completed)

        for i in range(len(words2) - 1, completed - 1, -1):
            # print(i, words1[len(words1) - len(words2) + i], words2[i])
            if words1[len(words1) - len(words2) + i] != words2[i]:
                return False

        return True


if __name__ == "__main__":
    inputs = [
        ("My name is Haley", "My Haley", ),
        ("of", "A lot of words", ),
        ("Eating right now", "Eating", ),
        ("Luky", "Lucccky", ),
        ("CwFfRo regR", "CwFfRo H regR", ),
    ]
    outputs = [
        (True),
        (False),
        (True),
        (False),
        (True),
    ]
    x = Solution()
    evaluate(x.areSentencesSimilar, inputs, outputs)
