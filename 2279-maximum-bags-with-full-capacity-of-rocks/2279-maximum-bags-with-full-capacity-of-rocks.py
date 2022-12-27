class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        arr=[]
        n=len(rocks)
        cnt=0
        for i in range(n):
            arr.append(capacity[i]-rocks[i])
        
        arr.sort()
        print(arr)
        for i in range(n):
            if additionalRocks<=0:
                break
            if arr[i]==0:
                cnt+=1
            
            else:
                if additionalRocks>=arr[i]:
                                      
                    additionalRocks -= arr[i]
                    cnt+=1
        return(cnt)