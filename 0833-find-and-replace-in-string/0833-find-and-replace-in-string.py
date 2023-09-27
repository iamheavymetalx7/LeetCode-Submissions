class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        new= ""
        # print(s)
        # print(indices,sources,targets)

        arr = list(zip(indices,sources,targets))
        arr.sort(key = lambda x:x[0])  
        # print(arr)
        k =len(indices)
        s=list(s)
        
        indices =[0 for _ in range(k)]
        sources= ["" for _ in range(k)]
        targets =["" for _ in range(k)]
        
        
        for i in range(k):
            indices[i] = arr[i][0]
            sources[i] = arr[i][1]
            targets[i] = arr[i][2]
        
        # print(indices,sources,targets,"this is new")
        
        for i in range(k):
            f=True
            v = indices[i]
            m = len(sources[i])
            # print(v,m)
            for j in range(0,m):
                # print(v+j,j,"here",sources[i])
                # print(s[v+j],sources[i][j])
                if v+j>=len(s):
                    f=False
                    break
                if s[v+j] != sources[i][j]:
                    f=False
                    break
            if f:
                new= targets[i]
                new_arr=[]
                new_len = m
                # print(new_len,"this is the new length",new)
                j=0
                for i in range(m-1):
                    new_arr.append(new[j:j+new_len])
                    j+=new_len
            
                
                new_arr.append(new[j:])
                
                print(new_arr)
                
                    
                s[v:v+m] = new_arr[:]
            # print(s)
        final =  ''.join(s)
        return (final)
                
                