#ACCEPTED(REVISIT)
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        mid = 0
        answer = 0
        while low<=high:
            mid = (low+high)//2
            if mid*mid==x:
                return mid
            elif mid*mid < x:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer

sol = Solution()
print(sol.mySqrt(8))