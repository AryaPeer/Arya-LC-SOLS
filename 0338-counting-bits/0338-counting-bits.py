class Solution:
    def countBits(self, n: int) -> List[int]:
        array = []
        
        for x in range(n+1):
            binary = bin(x)
            binary = binary[2:]
            
            counter = 0      
            
            for char in binary:
                if char =='1':
                    counter +=1
                    
            array.append(counter)
            
        return array