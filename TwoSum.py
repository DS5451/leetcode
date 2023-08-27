#ACCEPTED
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        check = {}
        for index, num in enumerate(nums):
            if target - num in check:
                return [check[target-num], index]

            check[num] = index
        return -1

sol = Solution()

print(sol.twoSum([2,4,6,8], 6))
