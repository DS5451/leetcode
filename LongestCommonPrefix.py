#ACCEPTED
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = [strs[0]]
      

        for s in strs:

            temp = ""
            flag = False
            for index, char in enumerate(s):
                length = len(prefix[0])
                if flag==False and index<length and char==prefix[0][index]:
                    temp+=char
                else:
                    flag = True
            prefix[0] = temp



        return prefix[0]

sol = Solution()

strs = ["cir", "car"]
str = "AAA"
print(sol.longestCommonPrefix(strs))
#
# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         Sorts Array
#         v=sorted(v)

#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans