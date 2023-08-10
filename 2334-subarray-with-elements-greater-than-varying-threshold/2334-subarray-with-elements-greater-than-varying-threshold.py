class UnionFind():
    def __init__(self,n):
        self.par = [i for i in range(n+1)]
        self.size= [1 for i in range(n+1)]

        self.mx=1
    def find(self,node):
        p=self.par[node]
        
        while p!=self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p=self.par[p]
        return p
    
    def merge(self,a,b):
        p1,p2=self.find(a),self.find(b)
        if p1==p2:
            return
        if self.size[p1]>self.size[p2]:
            p1,p2=p2,p1
        self.size[p2]+=self.size[p1]
        self.par[p1]=p2
        
        self.mx=max(self.mx,self.size[p2])
        
        
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        arr=[]
        
        for i,ele in enumerate(nums):
            arr.append((ele,i))
        arr.sort()
        # print(arr)
        
        
        active =[0]*(n)
        
        dsu = UnionFind(n)
        k=1
        j=n-1
        
        
        while j>=0 and k<=n:
            cur_thresh = threshold/k
            
            while j>=0 and arr[j][0]>cur_thresh:
                idx = arr[j][1]
                active[idx]=1
                if idx-1>=0 and active[idx-1]:

                    dsu.merge(idx,idx-1)

                if idx+1<n and active[idx+1]:

                    dsu.merge(idx,idx+1)


                j-=1
            if j<n-1 and dsu.mx>=k: ## j<n-1 states that there is atleast one active element
                return k 
            k+=1
        return -1
        
        
        
        