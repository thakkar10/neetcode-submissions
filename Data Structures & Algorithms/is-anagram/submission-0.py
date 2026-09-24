class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_1 = {}
        for letter in s:
            string_1[letter] = string_1.get(letter, 0) + 1
        
        string_2 = {}
        for letter in t:
            string_2[letter] = string_2.get(letter, 0) + 1

        if string_1 == string_2:
            return True
        else: 
            return False
