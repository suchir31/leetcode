class Solution(object):
    def answerString(self, word, num):
        if num==1:
            return word
        n=len(word)
        maxi=97
        ans=[]
        for i in range(n):
         if i+n-(num-1)<=n:
            ans.append(word[i:i+n-(num-1)])
         else:
            ans.append(word[i:])
        ans.sort()
        return ans[-1]