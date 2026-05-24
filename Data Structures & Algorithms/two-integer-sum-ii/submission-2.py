# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         prevMap={}
#         for i,n in enumerate(numbers):
#             diff=target-n
#             if n in prevMap:
#                 return [prevMap[n]+1,i+1]
#             prevMap[diff]=i
#         return []
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, (len(numbers)-1)
        
        while(l<r):
            curSum=numbers[l]+numbers[r]

            if(target<curSum):
                r=r-1
            elif(target>curSum):
                l=l+1
            else:
                return [l+1, r+1]
        return []
            
            
            
            
        
        
  



    

