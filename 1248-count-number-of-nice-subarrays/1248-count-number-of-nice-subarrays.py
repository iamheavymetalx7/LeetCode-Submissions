class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr=[0]

        cnt=0
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]%2
            if nums[i]%2==1:
                arr.append(i)
        arr.append(n)
        
        print(arr)
        
        m=len(arr)
        for i in range(1,m-1):
            if i+k<m:
                val1=(arr[i]-arr[i-1])+1 if i==1 else arr[i]-arr[i-1]
                val2= (arr[i+k]-arr[i+k-1])+1 if i==m-1 else arr[i+k]-arr[i+k-1]
                cnt+=val2*val1
        
        return (cnt)
                
                