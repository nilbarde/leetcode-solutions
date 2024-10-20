from leetcode import evaluate

class Solution:
    identifiers = ["&", "|", "!"]
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            return expression == "t"
        identifier_at = -1
        for i, key in enumerate(expression):
            if key in self.identifiers:
                identifier_at = i
            if key == ")":
                value = self.evaluate(expression[identifier_at:i+1])
                return self.parseBoolExpr(expression[:identifier_at] + value + expression[i+1:])
        return x

    def evaluate(self, expression):
        vals = [x=="t" for x in expression[2:-1].split(",")]
        result = True
        if expression[0] == "&":
            result = all(vals)
        elif expression[0] == "|":
            result = any(vals)
        else:
            result = not vals[0]
        if result:
            return "t"
        else:
            return "f"

if __name__ == "__main__":
    inputs = [
        ("&(|(f))", ),
        ("|(f,f,f,t)", ),
        ("!(&(f,t))", ),
    ]
    outputs = [
        (False),
        (True),
        (True),
    ]
    x = Solution()
    evaluate(x.parseBoolExpr, inputs, outputs)
