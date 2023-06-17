class Solution(object):
    def romanToInt(self, s):
        finalNumber = 0
        romanKey = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for letterPos in range(len(s)-1):
            currentLetter = romanKey[s[letterPos]]
            nextLetter = romanKey[s[letterPos + 1]]

            if nextLetter > currentLetter:
                finalNumber -= currentLetter
            else:
                finalNumber += currentLetter

        finalNumber += romanKey[s[-1]]

        return finalNumber
