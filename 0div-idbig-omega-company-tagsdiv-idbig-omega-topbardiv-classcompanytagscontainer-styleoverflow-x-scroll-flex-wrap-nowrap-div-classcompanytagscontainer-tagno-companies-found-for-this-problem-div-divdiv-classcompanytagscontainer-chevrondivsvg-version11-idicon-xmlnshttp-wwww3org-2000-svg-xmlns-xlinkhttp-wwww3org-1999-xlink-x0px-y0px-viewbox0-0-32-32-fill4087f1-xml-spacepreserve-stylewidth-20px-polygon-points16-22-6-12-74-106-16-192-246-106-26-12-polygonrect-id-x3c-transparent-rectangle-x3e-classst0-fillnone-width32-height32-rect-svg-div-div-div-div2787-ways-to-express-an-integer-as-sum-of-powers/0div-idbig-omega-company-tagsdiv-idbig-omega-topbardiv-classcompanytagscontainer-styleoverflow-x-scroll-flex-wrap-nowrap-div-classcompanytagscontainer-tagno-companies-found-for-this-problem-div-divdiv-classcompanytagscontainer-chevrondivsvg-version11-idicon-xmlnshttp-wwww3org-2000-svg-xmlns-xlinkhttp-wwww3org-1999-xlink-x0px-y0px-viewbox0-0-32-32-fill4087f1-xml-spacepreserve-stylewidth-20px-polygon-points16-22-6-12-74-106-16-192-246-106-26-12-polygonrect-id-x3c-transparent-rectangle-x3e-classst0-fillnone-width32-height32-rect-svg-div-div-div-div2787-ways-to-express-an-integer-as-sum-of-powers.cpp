class Solution {
public:
    int dp[301][301];
    int MOD = 1e9+7;
    int X;
    
    int Value(int val){
        int result =1 ;
        for (int i=0;i<X;i++){
            result*=val;
            if (result>300){
                return 301;
            }
                
        }
        return result;

    }
    
    int recur(int st,int val){
        if (val==0) return 1;
        if (st>300) return 0;
        
        if (dp[st][val]!=-1) return dp[st][val];
        int ans =0;
        if (Value(st)<=val){
            ans = (ans+recur(st+1,val-Value(st)))%MOD;
        }
        ans = (ans+recur(st+1,val))%MOD;
        
        return dp[st][val]=ans;
        
    }
    
    int numberOfWays(int n, int x) {
        X=x;
        memset(dp,-1,sizeof(dp));
        int val = recur(1,n);
        return val;
        
        
    }
};