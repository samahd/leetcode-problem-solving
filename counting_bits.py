class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for i in range(n+1):
            if ans[i]==0:
                if i%2==1:
                    ans[i]=1+ans[i//2]
                elif i%2==0:
                    ans[i]=ans[i//2]
        return ans
