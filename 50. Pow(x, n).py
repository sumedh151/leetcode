class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recurse(x, n):
            if n==0:
                return 1
            elif n==1:
                return x
            elif n%2==1:
                sq = recurse(x,n//2)
                return x * sq * sq
            else:
                sq = recurse(x,n//2)
                return sq * sq
        ans = recurse(x,abs(n))
        return ans if n>0 else 1/ans