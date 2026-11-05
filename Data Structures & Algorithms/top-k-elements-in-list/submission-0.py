class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_freq = {}

        for num in nums:
            if num not in number_freq:
                number_freq[num] = 1
            else:
                number_freq[num] += 1
        # we now how a frequency map of all numbers and the times they come up

        sorted_pairs = sorted(number_freq.items(), key = lambda pair: pair[1], reverse = True)
        # we now have the items sorted from greatest to least frequency
        return [pair[0] for pair in sorted_pairs[:k]]
        