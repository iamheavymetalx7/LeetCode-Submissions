class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        arr=[]
        for x in timePoints:
            new = x.split(":")
            hrs = int(new[0])*60
            mins = int(new[1])
            arr.append(hrs+mins)
            arr.append((24*60 + hrs)+mins)
        arr.sort()
        val = int(1e19)
        n=len(arr)
        for i in range(1,n):
            val = min(val, arr[i]-arr[i-1])
        return val