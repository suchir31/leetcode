maxi=0
def fun(i,dp,cur,nums,n):
    global maxi
    if i==n-1:
        return 0
    if dp[i][cur]!=-1:
           return dp[i][cur]
    ma=0
    for j in range(i+1,n):
        if abs(nums[i]-nums[j])<=cur:
            ma=max(1+fun(j,dp,abs(nums[i]-nums[j]),nums,n),ma)
    dp[i][cur]=ma
    maxi=max(maxi,dp[i][cur])
    return dp[i][cur] 
class Solution(object):
    def longestSubsequence(self, nums):
        global maxi
        maxi=0
        n=len(nums)
        dp=[[-1 for z in range(301)] for x in range(n)]
        for i in range(n-1):
            fun(i,dp,300,nums,n)
        return maxi+1
        