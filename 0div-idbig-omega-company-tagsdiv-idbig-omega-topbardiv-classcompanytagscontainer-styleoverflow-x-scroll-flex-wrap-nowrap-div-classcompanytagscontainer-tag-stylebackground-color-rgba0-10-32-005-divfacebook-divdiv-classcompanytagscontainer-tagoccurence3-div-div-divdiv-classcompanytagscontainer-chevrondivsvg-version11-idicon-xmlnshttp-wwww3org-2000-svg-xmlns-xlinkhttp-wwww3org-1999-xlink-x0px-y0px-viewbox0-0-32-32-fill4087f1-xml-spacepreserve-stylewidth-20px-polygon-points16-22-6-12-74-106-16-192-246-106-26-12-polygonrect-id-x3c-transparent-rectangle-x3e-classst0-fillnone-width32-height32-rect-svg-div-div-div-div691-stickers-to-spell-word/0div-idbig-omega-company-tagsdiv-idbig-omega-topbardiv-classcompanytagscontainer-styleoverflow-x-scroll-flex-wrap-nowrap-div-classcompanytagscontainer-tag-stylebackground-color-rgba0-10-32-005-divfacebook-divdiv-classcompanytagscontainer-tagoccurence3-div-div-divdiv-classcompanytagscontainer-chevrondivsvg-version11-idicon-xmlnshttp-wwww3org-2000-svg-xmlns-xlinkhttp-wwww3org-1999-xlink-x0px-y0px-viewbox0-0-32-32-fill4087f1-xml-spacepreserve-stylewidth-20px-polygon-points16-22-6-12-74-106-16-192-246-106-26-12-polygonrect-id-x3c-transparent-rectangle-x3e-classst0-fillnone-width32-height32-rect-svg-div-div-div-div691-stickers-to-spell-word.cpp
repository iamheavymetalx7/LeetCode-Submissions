class Solution {
public:
    vector<string> a;
    string t;
    int n,m,dp[1<<15];
    
    
    int recur(int mask){
        if (mask ==(1<<m)-1){
            return 0;
        }
        if (dp[mask]!=-1){return dp[mask];
                         }
        int ans = 1e9;
        for (int i=0;i<n;i++){
            vector<int> cnt(26,0);
            for (int j=0;j<a[i].size();j++){
                cnt[a[i][j]-'a']++;
            }
            int newmask =0;
            for (int j=0;j<m;j++){
                if (!(mask&(1<<j))){
                    if (cnt[t[j]-'a']>0){
                        cnt[t[j]-'a']--;
                        newmask |= (1<<j);
                    }
                }

                }
                if (newmask!=0){
                    ans = min(ans,1+recur(newmask|mask));
                
            }

        }           
        return dp[mask]=ans;

        
    }
    
    int minStickers(vector<string>& stickers, string target) {
        
        a = stickers;
        n = a.size();
        t = target;
        m= t.size();
        memset(dp,-1,sizeof(dp));
        
        int val = recur(0);
        
        if (val>=1e9){
            val=-1;
        }
        return val;
        
    }
};