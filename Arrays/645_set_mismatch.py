class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        totalSum = sum(nums)
        actualSum = sum(set(nums))

        dup = totalSum - actualSum
        miss = n * (n + 1) // 2 - actualSum

        return [dup, miss]