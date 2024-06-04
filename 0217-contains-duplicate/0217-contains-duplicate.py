class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val_set = set()
        
        for n in nums:
            if n in val_set:
                return True
            else:
                val_set.add(n)
                
        
        return False