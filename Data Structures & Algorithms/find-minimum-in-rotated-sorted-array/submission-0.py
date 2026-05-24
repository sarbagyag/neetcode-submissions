class Solution:
    def findMin(self, nums: List[int]) -> int:
        top=nums[0]
        length=len(nums)-1

        while(nums[length]<nums[0]):
            nums[0]=nums[length]
            length=length-1
        
        return nums[0]

      
        