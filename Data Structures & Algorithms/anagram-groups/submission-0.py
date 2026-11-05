class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        signature_freq = {}    
    
        for string in strs:
            word_freq = {}
            for char in string:
                if char not in word_freq:
                    word_freq[char] = 1
                else:
                    word_freq[char] += 1
            signature = tuple(sorted(word_freq.items()))
            
            if signature not in signature_freq:
                signature_freq[signature] = []
            
            signature_freq[signature].append(string)

        return list(signature_freq.values())
            

