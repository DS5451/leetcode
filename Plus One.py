#Accepted

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = ""
        for i in digits:
            a+=str(i)

        a = str(int(a)+1)
        b = []
        for i in a:
            b.append(int(i))

        return b



sol = Solution()

strs = [1, 1, 2]
print(sol.plusOne(strs))