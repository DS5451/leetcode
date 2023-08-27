#ACCEPTED
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:return 0
        if n == 1: return 1
        if n == 2: return 2

        steps = [0,1,2]

        for index in range(2, n):
            steps.append(steps[index-1]+steps[index])

        return steps[n]

sol = Solution()
print(sol.climbStairs(4))