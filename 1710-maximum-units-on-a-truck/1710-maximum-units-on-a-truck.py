class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x:-x[1])
        n=len(boxTypes)
        
        print(boxTypes)
        i=0
        curr=0
        ans=0
        while i<n and curr+boxTypes[i][0]<=truckSize:
            ans+=boxTypes[i][0]*boxTypes[i][1]
            curr+=boxTypes[i][0]
        
            i+=1
        if i<n:
            ans+=(truckSize - curr)*boxTypes[i][1]
            
        
        
        return ans