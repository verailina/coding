class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            max_size = min(len(s), len(prefix))
            i = 0
            while i < max_size:
                if s[i] != prefix[i]:
                    break
                i += 1
            prefix = prefix[:i]
            if prefix == "":
                break
                
        return prefix
        