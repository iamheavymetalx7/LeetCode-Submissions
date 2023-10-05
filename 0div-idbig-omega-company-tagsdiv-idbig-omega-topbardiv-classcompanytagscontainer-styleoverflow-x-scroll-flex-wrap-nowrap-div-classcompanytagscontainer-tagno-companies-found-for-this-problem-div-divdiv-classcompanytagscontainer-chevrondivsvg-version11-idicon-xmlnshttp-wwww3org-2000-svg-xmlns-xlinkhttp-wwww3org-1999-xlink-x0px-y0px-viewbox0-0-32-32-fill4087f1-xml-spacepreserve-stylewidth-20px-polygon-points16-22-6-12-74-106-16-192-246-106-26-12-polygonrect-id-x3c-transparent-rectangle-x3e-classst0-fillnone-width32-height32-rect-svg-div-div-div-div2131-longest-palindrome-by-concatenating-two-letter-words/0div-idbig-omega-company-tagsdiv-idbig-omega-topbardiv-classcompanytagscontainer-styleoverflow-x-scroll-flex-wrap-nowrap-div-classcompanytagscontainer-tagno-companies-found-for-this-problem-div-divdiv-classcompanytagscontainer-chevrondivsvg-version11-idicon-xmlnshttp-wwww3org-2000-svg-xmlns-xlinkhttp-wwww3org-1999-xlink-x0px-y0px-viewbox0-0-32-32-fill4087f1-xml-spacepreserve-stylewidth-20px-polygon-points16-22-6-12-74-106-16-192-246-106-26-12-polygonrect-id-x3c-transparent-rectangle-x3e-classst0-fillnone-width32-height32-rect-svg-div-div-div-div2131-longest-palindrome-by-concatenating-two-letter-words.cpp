class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        map<string,int> m;
        int unpaired =0;
        int ans =0;
        
        
        for(string w : words){
            if (w[0]==w[1]){
                if (m[w]>0){
                    unpaired--;
                    ans+=4;
                    m[w]--;
                }
                else{
                    m[w]+=1;
                    unpaired+=1;
                }
            }
        else{
            string rev=w;
            reverse(rev.begin(),rev.end());
            if (m[rev]>0){
                ans+=4;
                m[rev]-=1;
                
            }
            else{
                m[w]+=1;
            }
        }
        }
        if (unpaired){
            ans+=2;
        }
        return ans;
    }
};