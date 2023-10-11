class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        map<int,int> diff;
        diff[0]=0;
        
        for(auto f: flowers){
            diff[f[0]]+=1;
            diff[f[1]+1]-=1;
                
        }
        
        vector<int> positions;
        vector<int> prefix;
        
        int curr= 0;
        
        for (auto pair: diff){
            positions.push_back(pair.first);
            curr+=pair.second;
            prefix.push_back(curr);
        }
        
        vector<int> ans;
        
        for (auto person : people){
            int i = upper_bound(positions.begin(), positions.end(),person)-positions.begin()-1;
            ans.push_back(prefix[i]);
        }
        return ans;
    }
};