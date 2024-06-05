class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1),len(word2))
        
        combined = ""
        
        for x in range(length):
            combined += word1[x:x+1]
            combined += word2[x:x+1]
            
        if (len(word1)) > (len(word2)):
            combined += word1[length:]
        elif (len(word1)) < (len(word2)):
            combined += word2[length:]
            
        return combined
        