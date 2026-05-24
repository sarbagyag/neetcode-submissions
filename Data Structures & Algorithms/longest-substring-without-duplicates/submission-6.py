class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterSet=set()
        count=0
        l=0

        for r in range(len(s)):
            while s[r] in characterSet:
                characterSet.remove(s[l])
                l=l+1
            characterSet.add(s[r])
            count=max(count,r-l+1)
        return count

            




       