class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        for i in range(n+1):
            c=0
            n=i
            while n:
                n&=(n-1)
                c=c+1
            a.append(c)
        return a