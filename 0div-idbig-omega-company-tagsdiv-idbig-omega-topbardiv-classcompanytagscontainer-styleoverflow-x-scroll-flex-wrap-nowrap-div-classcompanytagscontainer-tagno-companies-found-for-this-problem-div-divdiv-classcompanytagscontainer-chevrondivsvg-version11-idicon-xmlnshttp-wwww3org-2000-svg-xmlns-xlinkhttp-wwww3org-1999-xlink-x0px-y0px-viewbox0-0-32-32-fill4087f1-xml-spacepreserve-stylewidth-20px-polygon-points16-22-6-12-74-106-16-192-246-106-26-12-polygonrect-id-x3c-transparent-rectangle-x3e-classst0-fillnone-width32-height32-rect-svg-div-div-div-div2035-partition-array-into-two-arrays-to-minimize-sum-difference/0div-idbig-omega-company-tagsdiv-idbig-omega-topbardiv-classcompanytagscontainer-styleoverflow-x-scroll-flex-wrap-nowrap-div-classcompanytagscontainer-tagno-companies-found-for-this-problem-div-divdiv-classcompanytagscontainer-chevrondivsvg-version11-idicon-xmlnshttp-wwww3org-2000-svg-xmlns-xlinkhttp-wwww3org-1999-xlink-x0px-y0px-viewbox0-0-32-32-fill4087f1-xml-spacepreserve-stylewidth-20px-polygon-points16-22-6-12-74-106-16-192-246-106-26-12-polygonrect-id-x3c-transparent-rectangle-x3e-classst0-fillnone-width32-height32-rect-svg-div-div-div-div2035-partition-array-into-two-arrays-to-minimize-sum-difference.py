class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        n=len(nums)

        
        def get_sums(l,r):
            length  = r-l+1
            arr =[[] for _ in range(length+1)]
            
            for i in range(1<<(length)):
                sum_,cnt=0,0
                for j in range(length):
                    if (i&(1<<j)):
                        sum_+=nums[l+j]
                        cnt+=1
                arr[cnt].append(sum_)
            return arr
        
        left = get_sums(0,n//2-1)
        right = get_sums(n//2,n-1)
        
        # print(left)
        # print(right)
        
        summ=sum(nums)
        target = summ//2

        ans=int(1e20)
        
        for i in range(n//2+1):
            right[n//2-i].sort()
            
            for j in range(0,len(left[i])):
                curr = left[i][j]
                
                idx = bisect_left(right[n//2-i],target-curr)
                if idx<len(right[n//2-i]):
                    ans=min(ans,abs(summ-2*(curr+right[n//2-i][idx])))
                if idx>0:
                    ans=min(ans,abs(summ-2*(curr+right[n//2-i][idx-1])))
        return ans
                
                        
                
            