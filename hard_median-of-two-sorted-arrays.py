# link -> https://leetcode.com/problems/median-of-two-sorted-arrays/

from leetcode import evaluate

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1, l2 = len(nums1), len(nums2)
        total_numbers = l1 + l2
        if total_numbers == 1:
            if l1:
                return nums1[0]
            else:
                return nums2[0]
        elif total_numbers == 2:
            return (sum(nums1) + sum(nums2)) / 2
        elif l1 == 0:
            i = int(l2 / 2)
            if l2 % 2 == 0:
                return (nums2[i] + nums2[i - 1]) / 2
            else:
                return nums2[i]
        elif l2 == 0:
            i = int(l1 / 2)
            if l1 % 2 == 0:
                return (nums1[i] + nums1[i - 1]) / 2
            else:
                return nums1[i]

        if nums1[0] < nums2[0]:
            i1 = 0
            i2 = -1
            curr = nums1[0]
        else:
            i1 = -1
            i2 = 0
            curr = nums2[0]
        prev = None
        moves = int(total_numbers / 2)
        # print(moves)
        for move_completed in range(moves):
            # print("---", i1, i2, prev, curr)
            if i1 == l1 - 1:
                i2 += 1
                prev, curr = curr, nums2[i2]
            elif i2 == l2 - 1:
                i1 += 1
                prev, curr = curr, nums1[i1]
            elif nums1[i1 + 1] < nums2[i2 + 1]:
                i1 += 1
                prev, curr = curr, nums1[i1]
            else:
                i2 += 1
                prev, curr = curr, nums2[i2]
            # print("***", i1, i2, prev, curr)
        if total_numbers % 2:
            return curr
        else:
            return (prev + curr) / 2

if __name__ == "__main__":
    inputs = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([1, 3, 5], [2, 4, 6]),
        ([1, 3, 5, 7, 8, 9, 10], [2, 4, 6]),
        ([1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15], [2, 4, 6]),
        ([1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], [2, 4, 6]),
        ([0,0,0,0,0], [-1,0,0,0,0,0,1])
    ]
    outputs = [
        2,
        2.5,
        3.5,
        5.5,
        8,
        9.5,
        0,
    ]
    x = Solution()
    evaluate(x.findMedianSortedArrays, inputs, outputs)
