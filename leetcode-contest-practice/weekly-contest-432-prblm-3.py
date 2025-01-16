from collections import defaultdict
def ispossible(vis,d,i,mid): 
    if not vis[i]:
        vis[i]=1
    else:
        return
    for j,le in d[i]:
        if le<=mid:
            ispossible(vis,d,j,mid)
    return
class Solution(object):
    def minMaxWeight(self, n, edges, threshold):
        mini=1
        maxi=10**6
        d=defaultdict(list)
        for i,j,le in edges:
            d[j].append([i,le])
        while mini<=maxi:
                mid=(mini+maxi)//2
                flag=0
                vis=[0 for x in range(n)]
                ispossible(vis,d,0,mid)
                flag=0
                for i in range(1,n):
                    if not vis[i]:
                        flag=1
                if flag==0:
                    maxi=mid-1
                else:
                    mini=mid+1  
        if mini>10**6:
            return -1
        return mini
