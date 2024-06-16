class Solution:
    def reverseVowels(self, s: str) -> str:
        loc = []
        charset = {'a','e','i','o','u','A','E','I','O','U'}
        returnval = ""
        
        for a in range(len(s)):
            x = s[a]
            if x in charset:
                loc.append(a)
                
        for a in range(len(s)):
            if s[a] not in charset:
                returnval += s[a]
            else:
                returnval += s[loc.pop()]
                
        return returnval
                
        
                
        
                
        
                
        