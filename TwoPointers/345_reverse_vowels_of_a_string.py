class Solution:
    def reverseVowels(self,s:str)->str:
        v="aeiouAEIOU"
        x=list(s)
        i=0
        j=len(x)-1
        while i<j:
            if x[i] in v and x[j] in v:
                x[i],x[j]=x[j],x[i]
                i+=1
                j-=1
            elif x[j] not in v:
                j-=1
            else:
                i+=1
        return "".join(x)