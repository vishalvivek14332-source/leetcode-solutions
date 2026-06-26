class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        xor=0
        for num in nums:
            freq[num] +=1
            if freq[num]==2:
                xor^=num
        return xor
