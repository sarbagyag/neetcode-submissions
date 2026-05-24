class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while(l<=r):  #the condition has to be (l<=r and not l<r because l=r ma pani answer lukeko huncha aka m=(l+l)/2)
            m=(l+r)//2

            if(nums[m]==target):
                return m

            elif(nums[m]>target):
                r=m-1

            else:
                l=m+1

        return -1
            
               

        
        