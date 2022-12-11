class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        grid2=[]
        for row in grid:
            grid2.append(sorted(row))
        print(grid2)
        to_ret = 0
        for j in range(len(grid2[0])-1,-1,-1):
            to_ret+=max(row[j] for row in grid2)
            
        return to_ret