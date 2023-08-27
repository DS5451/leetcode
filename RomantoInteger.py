#ACCEPTED
class Solution:
    def romanToInt(self, s: str) -> int:
        Values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number = 0
        prev_val = 0
        for index, i in enumerate(s):
            print(number)
            current = Values[i]

            if prev_val<current:
                number -= prev_val
                current-=prev_val

            number += current

            prev_val = current
        return number

Sol = Solution()
print(Sol.romanToInt('MCMXCIV'))



