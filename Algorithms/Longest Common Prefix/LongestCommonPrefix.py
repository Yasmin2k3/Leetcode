"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"."""

class Solution(object):
    def longestCommonPrefix(self, strs: [str]) -> str:
        outPut = ""

        for i in range(len(strs[0])):
            for a in strs:
                if i == len(a) or a[i] != strs[0][i]:
                    return outPut
            outPut += strs[0][i]

        return outPut

    strs = ["ab", "abacus", "abc"]
    print(longestCommonPrefix(0, strs))