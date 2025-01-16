from collections import defaultdict
class Solution(object):
    def calculateScore(self, s):
        d=defaultdict(list)
        n=len(s)
        ans=0
        for i in range(n):
            key=ord(s[i])-97
            if len(d[abs(25-key)])>0:
                print(key)
                k=d[25-key].pop()
                ans+=i-k
            else:
                d[key].append(i)
        return ans