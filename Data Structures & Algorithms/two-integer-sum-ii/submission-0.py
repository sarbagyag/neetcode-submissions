class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap={}
        for i,n in enumerate(numbers):
            diff=target-n
            if n in prevMap:
                return [prevMap[n]+1,i+1]
            prevMap[diff]=i
        return []
        
        




    

