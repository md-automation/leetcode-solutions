class Solution:
    
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        ans=[]

        if m*n==len(original):
            a=0

            for i in range(0,m):
                t=[]
                for j in range(0,n):
                    t.append(original[a])
                    a=a+1
                ans.append(t)

        return ans