class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        int mx,mn;
        mx=-1;
        mn=-1;
        
        int n = nums.size();
        vector<int> ans(2,-1);
        
        for (int i=0;i<n;i++){
            if (i>=indexDifference){
                if(mn==-1 || nums[i-indexDifference]<nums[mn]) {
                    mn = i-indexDifference;
                }
                
                if(mx==-1 || nums[i-indexDifference]>nums[mx]) {
                    mx = i - indexDifference;}
                
                
                if ((nums[i]-nums[mn])>=valueDifference){
                    ans[0]=mn;
                    ans[1]=i;
                    return ans;}
                if ((nums[mx]-nums[i])>=valueDifference){
                    ans[0]=i;
                    ans[1]=mx;
                    return ans;
                }
                
            }
        }
        return {-1,-1};
        
    }
};