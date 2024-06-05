class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ls = nums[:i]
            rs = nums[i+1:]
            
            if sum(ls) == sum(rs):
                return i
            
        return -1