class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':  # Check if there's a double digit followed by '#'
                decoded_char = chr(int(s[i:i+2]) + 96)  # Convert the double-digit number to a character
                i += 3  # Move three steps forward to skip the digits and '#'
            else:
                decoded_char = chr(int(s[i]) + 96)  # Convert the single digit to a character
                i += 1
                
            result.append(decoded_char)
        
        return ''.join(result)
