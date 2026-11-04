class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If strings aren't same size, impossible for anagram
        if len(s) != len(t):
            return False
        sFreq = {}
        tFreq = {}

        for char in s:
            if char not in sFreq:
                sFreq[char] = 1
            else:
                sFreq[char] += 1

        for char in t:
            if char not in tFreq:
                tFreq[char] = 1
            else:
                tFreq[char] += 1
        
        if tFreq == sFreq:
            return True
        return False