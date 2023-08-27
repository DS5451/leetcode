#INCOMPLETE
#review kmp algo will be hard but who knows

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return -1

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

sol = Solution()
str = "hello"
print(sol.strStr(str,"ello"))