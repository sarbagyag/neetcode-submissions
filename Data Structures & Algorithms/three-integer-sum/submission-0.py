class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]

        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            target=-nums[i]

            while l<r:
                if nums[l]+nums[r]>target:
                    r=r-1
                elif nums[l]+nums[r]<target:
                    l=l+1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l=l+1
                    r=r-1

                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
                    while l<r and nums[r]==nums[r+1]:
                        r=r-1
        return result
                  



    


        
           
