def lcm(a,b):
    if a%b==0 or b%a==0:
        return max(a,b)
    else:
        return a*b//gcd(min(a,b),max(a,b))
def gcd(a,b):
    #print(a,b)
    if b%a==0:
        return a
    else:
        return gcd(b%a,a)
class Solution(object):
    def maxLength(self, nums):
        n=len(nums)
        maxi=0
        for i in range(n):
            for j in range(i+1,n):
                prod=1
                g=nums[i]
                l=nums[i]
                for k in range(i,j+1):
                    prod=prod*nums[k]
                    #print(g,nums[k],"p")
                    g=gcd(g,nums[k])
                    l=lcm(l,nums[k])
                if prod==g*l:
                    maxi=max(j+1-i,maxi)
        return maxi