class Solution(object):
    def hasMatch(self, s, p):
        for i in range(len(p)):
            if p[i]=="*":
                break
        s1=p[:i]
        s2=p[i+1:]
        for i in range(len(s)-len(s1)+1):
            #print(s1,s[i:i+len(s1)])
            if s1==s[i:i+len(s1)]:
                for j in range(i+len(s1),len(s)-len(s2)+1):
                    #print(s1,s2,s[j:j+len(s2)])
                    if s2==s[j:j+len(s2)]:
                        return True
        return False