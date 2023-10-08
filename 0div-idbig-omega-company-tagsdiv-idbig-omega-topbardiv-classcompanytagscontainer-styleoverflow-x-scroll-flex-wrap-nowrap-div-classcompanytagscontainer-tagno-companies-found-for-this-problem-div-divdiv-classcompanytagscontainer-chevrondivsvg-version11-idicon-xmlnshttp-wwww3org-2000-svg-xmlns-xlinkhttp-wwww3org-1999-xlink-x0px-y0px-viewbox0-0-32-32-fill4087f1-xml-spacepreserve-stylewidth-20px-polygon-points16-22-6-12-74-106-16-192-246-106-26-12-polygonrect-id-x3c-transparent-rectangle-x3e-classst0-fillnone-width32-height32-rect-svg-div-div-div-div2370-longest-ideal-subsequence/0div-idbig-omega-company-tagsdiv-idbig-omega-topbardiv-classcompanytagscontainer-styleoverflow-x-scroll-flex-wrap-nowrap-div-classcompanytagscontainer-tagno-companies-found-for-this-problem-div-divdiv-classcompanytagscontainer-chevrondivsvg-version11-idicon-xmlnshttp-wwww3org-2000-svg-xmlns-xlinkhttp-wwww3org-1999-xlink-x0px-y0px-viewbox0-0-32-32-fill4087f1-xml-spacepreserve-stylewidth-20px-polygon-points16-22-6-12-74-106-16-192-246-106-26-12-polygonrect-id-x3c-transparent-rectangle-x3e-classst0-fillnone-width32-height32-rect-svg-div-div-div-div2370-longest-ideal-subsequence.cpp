class Solution {
public:
    int dp[100005][150];
    
    int recur(string &s,int idx, int prev,int &k){
        if (idx>=s.size()){
            return 0;
        }
        if (dp[idx][prev]!=-1){
            return dp[idx][prev];
    }
        int inc=0;
        int notinc=0;
        if (prev==0 || abs(s[idx]-prev)<=k){
            inc = 1+recur(s,idx+1,s[idx],k);
        }
        notinc = recur(s,idx+1,prev,k);
        
        return dp[idx][prev] = max(inc,notinc);
    }
    
    int longestIdealString(string s, int k) {
        int ans;
        memset(dp,-1,sizeof(dp));
        ans = recur(s,0,0,k);
        return ans;
    }
};