"""An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """