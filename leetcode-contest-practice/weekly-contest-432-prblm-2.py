class Solution(object):
    def maximumAmount(self, nums):
        n=len(nums)
        m=len(nums[0])
        dp=[[[-99999999 for x in range(3)]for y in range(m+1)]for z in range(n+1)]
        dp[0][0][0],dp[0][1][0],dp[1][0][0]=0,0,0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums[i-1][j-1]>0:
                    dp[i][j][0]=max(dp[i-1][j][0],dp[i][j-1][0])+nums[i-1][j-1]
                    if max(dp[i-1][j][1],dp[i][j-1][1])>-99999999:
                        dp[i][j][1]=max(dp[i-1][j][1],dp[i][j-1][1])+nums[i-1][j-1]
                    if max(dp[i-1][j][2],dp[i][j-1][2])>-99999999:
                        dp[i][j][2]=max(dp[i-1][j][2],dp[i][j-1][2])+nums[i-1][j-1]
                else:
                    dp[i][j][1]=max(max(dp[i-1][j][0],dp[i][j-1][0]),max(dp[i-1][j][1],dp[i][j-1][1])+nums[i-1][j-1])
                    if max(dp[i-1][j][1],dp[i][j-1][1])>-99999999:
                        dp[i][j][2]=max(max(dp[i-1][j][1],dp[i][j-1][1]),max(dp[i-1][j][2],dp[i][j-1][2])+nums[i-1][j-1])
                    dp[i][j][0]=max(dp[i-1][j][0],dp[i][j-1][0])+nums[i-1][j-1]
        #print(dp) 
        return max(dp[-1][-1])