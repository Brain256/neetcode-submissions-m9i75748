class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        nums = []


        i = 0
        j = 0

        d = 1

        while len(nums) < (len(matrix) * len(matrix[0])): 
            nums.append(matrix[i][j])

            if d == 1: 
                if j == right: 
                    d = 2
                    i += 1
                    top += 1
                else: 
                    j += 1

            elif d == 2: 
                if i == bottom: 
                    d = 3
                    j -= 1
                    right -= 1
                else: 
                    i += 1

            elif d == 3:
                if j == left: 
                    d = 4
                    i -= 1
                    bottom -= 1
                else: 
                    j -= 1

            else: 
                if i == top: 
                    d = 1
                    j += 1
                    left += 1
                else: 
                    i -= 1
        
        return nums