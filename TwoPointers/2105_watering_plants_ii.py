class Solution:
    def minimumRefill(self,plants:List[int],capacityA:int,capacityB:int)->int:
        r=0
        i=0
        j=len(plants)-1
        a=capacityA
        b=capacityB

        while i<j:
            if plants[i]>a:
                r+=1
                a=capacityA
            a-=plants[i]

            if plants[j]>b:
                r+=1
                b=capacityB
            b-=plants[j]

            i+=1
            j-=1

        if i==j:
            if max(a,b)<plants[i]:
                r+=1

        return r