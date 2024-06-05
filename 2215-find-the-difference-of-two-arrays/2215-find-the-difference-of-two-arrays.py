class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        
        set1 = set()
        set2 = set()
        set3 = set()
        set4 = set()
        
        nums1.sort()
        nums2.sort()
        
        for x in nums1:
            set1.add(x)
            
        for x in nums2:
            if x not in set1:
                set3.add(x)
                
            set2.add(x)
            
        for x in nums1:
            if x not in set2:
                set4.add(x)
                
        return [list(set4), list(set3)]