class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cp = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return cp
            cp += strs[0][i]
        return cp