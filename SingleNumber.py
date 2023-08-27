#Use XOR because this will cancel out duplicates due to it being the same binary value
#
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result



# Define a test case
test_case = [4, 1, 2, 1, 2]

# Test the Solution class
solution = Solution()
result = solution.singleNumber(test_case)

print("Input:", test_case)
print("Output:", result)