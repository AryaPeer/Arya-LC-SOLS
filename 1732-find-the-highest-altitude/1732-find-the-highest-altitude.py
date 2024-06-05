class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        newList = [0,]
        
        for i in range(len(gain)):
            if i == 0:
                newList.append(gain[i])
            else:
                newList.append(gain[i] + newList[i])
            
        return max(newList)