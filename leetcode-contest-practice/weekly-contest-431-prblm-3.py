import bisect
class Solution(object):
    def maximumCoins(self, coins, k):
        coins.sort()
        n=len(coins)
        ci=[]
        p=[]
        ans=0
        ri=[]
        for l,r,c in coins:
            ci.append(l)
            ri.append(r)
            p.append((r-l+1)*c)
        for i in range(1,n):
            p[i]+=p[i-1]
        #print(coins)
        cou=0
        maxi=0
        #print(p)
        for l,r,c in coins:
            #print(l)
            x=bisect.bisect_right(ci,l+k-1,0,n)
            x=x-1
            if cou>0:
                   ans+=p[x]-p[cou-1]
            else:
                    ans+=p[x]
            if coins[x][1]>l+k-1:
                   #print(ans,"p")
                   ans-=(coins[x][1]-(l+k-1))*coins[x][2]
                   #print(ans)
            #print(x,l,l+k-1,ans)
            cou+=1
            maxi=max(maxi,ans)
            ans=0
            #print(cou,"cou",maxi)
        for l,r,c in coins[::-1]:
            #print(l)
            x=bisect.bisect_left(ri,r-k+1,0,n)
            x=x
            if x>0:
                   ans+=p[cou-1]-p[x-1]
            else:
                    ans+=p[cou-1]
            if coins[x][0]<r-k+1:
                   #print(ans,"p")
                   ans-=(r-k+1-coins[x][0])*coins[x][2]
                   #print(ans)
            #print(x,r,r-k+1,cou,ans)
            cou-=1
            maxi=max(maxi,ans)
            ans=0
            #print(cou,"cou",maxi)
        return maxi
