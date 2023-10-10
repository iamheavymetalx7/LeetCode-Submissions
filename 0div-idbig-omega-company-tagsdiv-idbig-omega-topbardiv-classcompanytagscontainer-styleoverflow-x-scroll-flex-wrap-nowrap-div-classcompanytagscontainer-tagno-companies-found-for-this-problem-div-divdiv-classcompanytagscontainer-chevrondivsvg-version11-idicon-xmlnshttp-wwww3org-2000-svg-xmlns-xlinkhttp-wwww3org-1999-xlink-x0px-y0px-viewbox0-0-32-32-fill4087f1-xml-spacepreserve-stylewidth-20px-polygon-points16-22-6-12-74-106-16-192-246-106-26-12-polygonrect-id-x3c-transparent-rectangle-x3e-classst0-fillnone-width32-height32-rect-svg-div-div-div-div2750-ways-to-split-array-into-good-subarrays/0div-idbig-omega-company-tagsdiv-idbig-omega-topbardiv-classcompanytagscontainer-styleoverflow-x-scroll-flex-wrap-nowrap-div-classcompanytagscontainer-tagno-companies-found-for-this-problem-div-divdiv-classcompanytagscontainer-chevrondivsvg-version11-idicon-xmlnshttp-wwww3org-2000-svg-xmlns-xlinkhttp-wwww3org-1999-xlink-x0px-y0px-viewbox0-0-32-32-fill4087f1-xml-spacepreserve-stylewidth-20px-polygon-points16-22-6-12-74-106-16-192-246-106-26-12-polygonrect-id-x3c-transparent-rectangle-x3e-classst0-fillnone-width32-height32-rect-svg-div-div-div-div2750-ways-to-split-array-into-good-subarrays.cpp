class Solution {
public:
    int dp[100005][2];
    int mod = 1e9+7;
    int n;
    int recur(int idx, int cnt, vector<int> & nums){
        if (idx>=n){
            if (cnt==1){return 1;}
            return 0;
        }

        
        cnt += (nums[idx]==1);
        if (cnt>1){
            return 0;
        }
        
        
        if (dp[idx][cnt]!=-1){
            return dp[idx][cnt];
        }
        int take=0;
        int nottake=0;
        take =recur(idx+1,cnt,nums);
        if (cnt==1){
            nottake = recur(idx+1,0,nums);
        }
        
        return dp[idx][cnt] = (take+nottake)%mod;
        
    }
    
    int numberOfGoodSubarraySplits(vector<int>& nums) {
        n = nums.size();
        memset(dp,-1,sizeof(dp));
        int val = recur(0,0,nums);
        return val%mod;
    }
};