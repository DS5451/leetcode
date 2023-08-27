
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
       a = sorted(list(set(nums)))
       nums.clear()
       for num in a:
           nums.append(num)

       print(nums)
       return len(a)

sol = Solution()

strs = [-1,1,2]
print(sol.removeDuplicates(strs))