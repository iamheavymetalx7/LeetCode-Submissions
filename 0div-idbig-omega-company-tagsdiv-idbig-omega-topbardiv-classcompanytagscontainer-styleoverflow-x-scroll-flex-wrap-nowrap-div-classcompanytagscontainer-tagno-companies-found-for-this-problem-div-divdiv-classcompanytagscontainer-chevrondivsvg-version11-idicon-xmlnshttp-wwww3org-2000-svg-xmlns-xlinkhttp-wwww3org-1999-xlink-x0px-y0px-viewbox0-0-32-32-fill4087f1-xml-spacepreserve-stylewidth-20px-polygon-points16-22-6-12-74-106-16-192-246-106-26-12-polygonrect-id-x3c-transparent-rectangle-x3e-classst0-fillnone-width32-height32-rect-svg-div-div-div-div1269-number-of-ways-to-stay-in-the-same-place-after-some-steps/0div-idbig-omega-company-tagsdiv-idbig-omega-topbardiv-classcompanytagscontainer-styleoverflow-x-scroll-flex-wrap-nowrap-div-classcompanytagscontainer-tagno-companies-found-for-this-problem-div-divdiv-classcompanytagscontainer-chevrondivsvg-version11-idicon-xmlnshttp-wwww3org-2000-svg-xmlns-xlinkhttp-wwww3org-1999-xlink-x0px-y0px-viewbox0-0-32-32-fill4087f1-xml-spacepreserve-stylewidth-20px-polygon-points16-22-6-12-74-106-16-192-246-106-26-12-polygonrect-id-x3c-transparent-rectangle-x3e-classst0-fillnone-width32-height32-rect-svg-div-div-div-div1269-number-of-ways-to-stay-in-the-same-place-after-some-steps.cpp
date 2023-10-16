class Solution {
public:
    vector<vector<int>> dp;
    int MOD = 1e9+7;
    int maxi;
    int recur(int idx,int rem){
        if (rem==0){
            if (idx==0){
                return 1;
            }
            return 0;
        }
        
        if (dp[idx][rem]!=-1){
            return dp[idx][rem];
        }
        
        int ans =0;
        ans = (ans+recur(idx,rem-1))%MOD;
        if (idx>0){
            ans = (ans+recur(idx-1,rem-1))%MOD;
        }
        if (idx<maxi-1){
            ans = (ans+recur(idx+1,rem-1))%MOD;
        }
        return dp[idx][rem] = ans;
    }
    
    int numWays(int steps, int arrLen) {
        dp = vector(501,vector(steps+1,-1));
        maxi = arrLen;
        int val = recur(0,steps);
        return val;
        
    }
};