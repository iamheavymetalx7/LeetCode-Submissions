class Solution {
public:
    int dp[501][501];
    int n;
    int recur(int i,int rem,vector<int> & cost, vector<int> & time){
        if (rem<=0) return 0;
        if (i>=n) return 1e9;
        if (dp[i][rem]!=-1) return dp[i][rem];
        int ans = 1e9;
        ans = min(ans,cost[i]+recur(i+1,rem-1-time[i],cost,time));
        ans = min(ans,recur(i+1,rem,cost,time));
        return dp[i][rem]=ans;
    }
    
    int paintWalls(vector<int>& cost, vector<int>& time) {
        n = cost.size();
        memset(dp,-1,sizeof(dp));
        return recur(0,n,cost,time);
    }
};