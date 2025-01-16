class Solution(object):
    def minimumOperations(self, grid):
        ans=0
        n=len(grid)
        m=len(grid[0])
        for i in range(m):
            for j in range(1,n):
                 #print(j,i)
                 if grid[j][i]-grid[j-1][i]<=0:
                    ans+=abs(grid[j][i]-grid[j-1][i])+1
                    grid[j][i]=grid[j-1][i]+1
        return ans