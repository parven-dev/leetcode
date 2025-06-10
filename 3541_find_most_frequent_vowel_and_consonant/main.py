class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowels = ["a", "e", "i", "o", "u"]
        consonants_dict = {}
        vowels_dict = {}

        for i in range(len(s)):
            if s[i] in vowels:
                vowels_dict[s[i]] = vowels_dict.get(s[i], 0) + 1
            else:
                consonants_dict[s[i]] = consonants_dict.get(s[i], 0) + 1
 

        max_consonant = max(consonants_dict.values()) if consonants_dict else 0

        max_vowel = max(vowels_dict.values()) if vowels_dict else 0

        return max_consonant + max_vowel
    
