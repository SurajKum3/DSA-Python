#  -> I started by assuming the first string as the prefix and iteratively reduce it while comparing with each subsequent string until it matches the beginning of all strings.

#  -> Time Complexity : O(n*m) - Where N is the number of strings and M is the length of the shortest string. In the worst case, the prefix is shortened character by character for each string.

#  -> Space Complexity : O(1) - No extra data structures are used - only a few variables to track the prefix and its length.👇

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len]
        
        return pref