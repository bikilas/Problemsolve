from collections import Counter

class Solution:
    def commonChars(self, words):
        if not words:
            return []

        # Count characters in the first word
        char_count = Counter(words[0])

        # Iterate through the rest of the words and update the character count
        for word in words[1:]:
            word_count = Counter(word)
            for char in char_count:
                char_count[char] = min(char_count[char], word_count[char])

        # Construct the result list
        result = []
        for char, count in char_count.items():
            result.extend([char] * count)

        return result

