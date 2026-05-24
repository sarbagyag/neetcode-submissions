class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q=collections.deque()
        l=r=0

        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop() #jabasamma last element nums[r] bhanda sano chha, pop.
            q.append(r)

            if l>q[0]:
                q.popleft() #removing out of scope of window elements from deque
            
            if(r+1)>=k: #initial check window size hanyo ki nai vanera 
                output.append(nums[q[0]])
                l=l+1 #append garepachi balla left pointer lai badhaune
            r=r+1
        return output
            
                
            
        