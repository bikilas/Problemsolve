class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Iterate through characters of the first string
        for i, char in enumerate(strs[0]):
            # Check if the character is present in the same position in all other strings
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]
        
        return strs[0]



