class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

    # now we have a counter of how many times a number has appeared
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                return True
        return False
        
        