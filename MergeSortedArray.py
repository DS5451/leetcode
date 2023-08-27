#WORKS BACKWARDS COMPARING VALUES FROM NUMS1
#First if statement is used to check if values from nums are not greater
#if the statement is true it will begin shifting elements to the left
#the else statement will place the values from nums 2 in 
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        p1, p2, p = m - 1, n - 1, m + n - 1


        while p1 >= 0 and p2 >= 0:

            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            print("nums:", nums1, "p:", p, "p1:", p1, "p2:", p2, )

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

    # def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    #     if len(nums2)!=0:
    #         n2 = 0
    #         for n1 in range(len(nums1)):
    #             if n2<len(nums2) and nums1[n1]>nums2[n2] and n1==0:
    #                 nums1.pop()
    #                 nums1.insert(n1, nums2[n2])
    #                 nums2.remove((nums2[n2]))
    #                 n2 += 1
    #             elif n2<len(nums2) and nums1[n1]<nums2[n2] and nums1[n1]+1>=nums2[n2]:
    #                 nums1.pop()
    #                 nums1.insert(n1+1, nums2[n2])
    #                 nums2.remove((nums2[n2]))
    #                 n2+=1
    #
    #     if len(nums2) != 0:
    #         for i in nums2:
    #             nums1.pop()
    #
    #         for i in nums2:
    #             nums1.append(i)




sol = Solution()
nums1 = [1,2,3,0,0,0]
sol.merge(nums1,3 , [2,5,6], 3)
print(nums1)