class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        binary = binary[2:]
        
        count = 0
        
        for char in binary:
            if char == '1':
                count += 1
                
        return count
                