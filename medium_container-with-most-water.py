from leetcode import evaluate

class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        i, j = 0, len(height)-1
        max_front, max_back = height[i] - 1, height[j] - 1
        while i < j:
            if height[i] < max_front:
                i += 1
                continue
            max_front = height[i]
            while j > i:
                if height[j] < max_back:
                    j -= 1
                    continue
                max_back = height[j]
                max_area = max(max_area, min(max_front, max_back) * (j-i))
                if max_area >= (j-i) * max_front:
                    break
                j -= 1
            i += 1
        return max_area

    def maxAreaV1(self, height) -> int:
        max_area = 0
        max_height_so_far = height[0] - 1
        for i in range(len(height)-1):
            if height[i] < max_height_so_far:
                continue
            max_height_so_far = height[i]
            if max_area >= (len(height)-1-i) * height[i]:
                continue
            for j in range(len(height)-1, i, -1):
                max_area = max(max_area, min(height[i], height[j]) * (j-i))
                if max_area >= (j-i) * height[i]:
                    break
        return max_area

if __name__ == "__main__":
    inputs = [
        ([1,8,6,2,5,4,8,3,7], ),
        ([1,1], ),
    ]
    outputs = [
        (49),
        (1),
    ]
    x = Solution()
    evaluate(x.maxArea, inputs, outputs)
