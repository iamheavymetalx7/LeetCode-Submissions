class Solution {
public:
    int dp[1005];
    int n;
    int recur(int idx,vector<int>& cost){
        if (idx>=n){
            return 0;
        }
        if (dp[idx]!=-1){return dp[idx];}
        int ans = 999*1000+10;
        ans = min(ans,cost[idx]+recur(idx+1,cost));
        ans = min(ans,cost[idx]+recur(idx+2,cost));
        return dp[idx] =ans;
    }
    
    
    int minCostClimbingStairs(vector<int>& cost) {
        memset(dp,-1,sizeof(dp));
        n = cost.size();
        int val = min(recur(0,cost),recur(1,cost));
        return val;
    }
};