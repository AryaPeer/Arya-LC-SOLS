class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        set1 = set()
        
        for x in nums:
            if x not in set1:
                set1.add(x)
            else:
                set1.remove(x)
                
        return set1.pop()