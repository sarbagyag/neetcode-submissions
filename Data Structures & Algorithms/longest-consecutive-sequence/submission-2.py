class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numSet=set(nums)

        for n in nums:
            #checking if the number 'n' is the start of the sequence
            if (n-1) not in numSet:
                length=0
                while(n+length in numSet):
                    length=length+1
                longest=max(longest, length)
        return longest
                
                
        