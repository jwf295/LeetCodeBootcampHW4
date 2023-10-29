class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if (s == ""):
            return 0
        stack = []
        counter = 0
        for c in s:
            if c == '(':
                stack.append(c)
                counter += 1
            else:
                if len(stack) == 0:
                    counter += 1
                elif stack.pop() == '(':
                    counter -= 1
                else:
                    counter += 1
        return counter
