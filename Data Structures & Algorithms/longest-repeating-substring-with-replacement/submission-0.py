class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        repChar = {}
        result = 0
        l = 0
        
        for r, ch in enumerate(s):
            repChar[ch] = 1 + repChar.get(ch, 0)
            
            while (r - l + 1) - max(repChar.values()) > k:
                repChar[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
        
        return result
