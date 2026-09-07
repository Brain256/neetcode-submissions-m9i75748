class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRows = set()
        zeroCols = set()

        for i in range(len(matrix)): 
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: 
                    zeroRows.add(i)
                    zeroCols.add(j)

        for r in zeroRows: 
            for z in range(len(matrix[0])): 
                matrix[r][z] = 0
        
        for c in zeroCols: 
            for z in range(len(matrix)): 
                matrix[z][c] = 0
        
        