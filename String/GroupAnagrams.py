#  -> I used a 26-length character frequency array as a key to group anagrams instead of sorting strings.
#  -> Time Complexity : O(nk) - For n strings of maximum length k, counting characters takes O(n · k) time.
#  -> Space Complexity : O(nk) - Hash map storage for frequency keys and grouped strings results in O(n · k) space.👇

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        
        return list(ans.values())