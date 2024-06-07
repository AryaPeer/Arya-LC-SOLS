class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed_str = ""
        current_char = ' '
        char_count = 0
        
        for char in chars:
            if current_char == ' ':
                current_char = char
                char_count += 1
                compressed_str += current_char
            else:
                if char == current_char:
                    char_count += 1
                else:
                    if char_count != 1:
                        compressed_str += str(char_count)
                    current_char = char
                    char_count = 1
                    compressed_str += current_char
        
        if char_count != 1:
            compressed_str += str(char_count)
        
        for i in range(len(compressed_str)):
            chars[i] = compressed_str[i]
        
        return len(compressed_str)