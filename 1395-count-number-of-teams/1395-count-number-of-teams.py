'''
since n=10^3
max time complexity : N^2

Dp x
Monotonic stack x


// recursion, brute force
N^3 -> N^2
        
        # print(nextgreater, nextlesser)
        
            # ng nl
        # 1 0 0
        # 4 0 1
        # 3 1 1
        # 5 0 3
        # 2 3 1

'''
class Solution:
    def numTeams(self, r: List[int]) -> int:
        n=len(r)
        nextgreater =[0]*(n)
        nextlesser = [0]*(n)
        arr=[r[-1]]
        
        for i in range(n-2,-1,-1):
            idx = bisect.bisect_left(arr,r[i])
            # print(r[i],idx)
            nextgreater[i] = 0 if idx==len(arr) else len(arr)-idx
            nextlesser[i] = idx
            arr.append(r[i])
            arr.sort()
        
        # print(nextgreater)
        # print(nextlesser)
        
        ans =0
        for i in range(n):
            for j in range(i+1,n):
                
                if r[i]>r[j]:
                    # print(r[i],r[j],nextlesser[j])
                    ans+= nextlesser[j]
                elif r[i]<r[j]:
                    # print(r[i],r[j],nextgreater[j],"this is greater")
                    ans+= nextgreater[j]
        return ans
