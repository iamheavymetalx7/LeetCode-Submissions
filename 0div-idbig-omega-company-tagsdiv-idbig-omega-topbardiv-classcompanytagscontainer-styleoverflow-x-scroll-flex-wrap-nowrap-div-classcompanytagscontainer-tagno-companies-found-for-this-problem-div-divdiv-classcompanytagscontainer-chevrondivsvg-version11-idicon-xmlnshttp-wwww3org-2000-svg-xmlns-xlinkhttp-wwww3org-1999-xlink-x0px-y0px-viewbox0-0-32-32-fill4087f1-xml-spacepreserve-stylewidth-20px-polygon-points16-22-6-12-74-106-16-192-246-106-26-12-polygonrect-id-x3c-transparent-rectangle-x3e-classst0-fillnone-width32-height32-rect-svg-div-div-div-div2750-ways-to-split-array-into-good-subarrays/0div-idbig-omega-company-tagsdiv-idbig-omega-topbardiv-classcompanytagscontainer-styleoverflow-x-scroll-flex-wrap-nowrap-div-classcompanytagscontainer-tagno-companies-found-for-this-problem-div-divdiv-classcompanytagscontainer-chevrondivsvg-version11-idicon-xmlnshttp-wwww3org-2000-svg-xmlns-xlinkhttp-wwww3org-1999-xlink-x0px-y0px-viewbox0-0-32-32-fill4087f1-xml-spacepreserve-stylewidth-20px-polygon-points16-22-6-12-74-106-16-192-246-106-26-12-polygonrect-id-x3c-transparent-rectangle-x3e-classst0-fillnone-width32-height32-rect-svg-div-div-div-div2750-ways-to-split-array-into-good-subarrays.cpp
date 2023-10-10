class Solution {
public:
    int mod = 1e9+7;
    int n;

    int recur(int idx, int cnt, vector<int> & nums, vector<vector<int>> & dp){
        if (idx<0){
            if (cnt==1) return 1;
            
            return 0;
        }
        

        
        if (nums[idx]==1)
            cnt++;
        
        if (cnt>1){
            return 0;
        }
        if (dp[idx][cnt]!=-1){
            return dp[idx][cnt];
        }
        
        int nottake=0;
        int take =recur(idx-1,cnt,nums,dp);
        if (cnt==1){
            nottake = recur(idx-1,0,nums,dp);
        }
        
        return dp[idx][cnt] = (take+nottake)%mod;
        
    }
    
    int numberOfGoodSubarraySplits(vector<int>& nums) {
        n = nums.size();
        vector<vector<int>> dp(n, vector<int>(2,-1));

        return recur(n-1,0,nums,dp);
    }
};