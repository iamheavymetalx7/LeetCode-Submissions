class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums)%p
        if need ==0:
            return 0
        print(need,"dfscdscsd")
        n=len(nums)
        res=n
        dic=defaultdict(int)
        dic[0]=-1
        cur= 0
        for i in range(n):
            cur=(cur+nums[i])%p
            
            if (cur-need)%p in dic:
                res = min(res,i-dic[(cur-need)%p])
            dic[cur]=i

        return res if res<n else -1