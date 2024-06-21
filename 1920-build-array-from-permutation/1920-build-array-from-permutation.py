class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        returnarr = [];
        
        for i in range(len(nums)):
            returnarr.append(nums[nums[i]])
            
        return returnarr