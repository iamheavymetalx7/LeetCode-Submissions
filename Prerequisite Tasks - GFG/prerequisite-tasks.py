#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        
        adj=defaultdict(list)
        for preq in prerequisites:
            adj[preq[0]].append(preq[1])
        # print(adj)
        indegree=[0]*N
        q=deque()
        topo=[]
        
        for i in range(N):
            for adjele in adj[i]:
                indegree[adjele]+=1
        
        for i in range(N):
            if indegree[i]==0:
                q.append(i)
                
        while q:
            node=q.popleft()
            topo.append(node)
            
            for adjele in adj[node]:
                indegree[adjele]-=1
                
                if indegree[adjele]==0:
                    q.append(adjele)
                    
        if len(topo)==N:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends