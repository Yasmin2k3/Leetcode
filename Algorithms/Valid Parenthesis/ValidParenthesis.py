"""An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

class Solution(object):
    def isValid(self, s: str) -> bool:
        li = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for p in s:
            if p in closeToOpen:
                if li and li[-1] == closeToOpen[p]:
                    li.pop()
                else:
                    return False
            else:
                li.append(p)

        if not li:
            return True
        else:
            return False

