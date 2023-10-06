class Solution {
vector<int> dp;

public:
    int integerBreak(int n) {
        if (n<=3){
            return n-1;
        }
        dp.resize(60,-1);
        int val;
        val = recur(n);
        return val;
    }
int recur(int n){
if (n==0){
    return 1;
}
if (n<0){
    return 0;
}
if (n==2){
    return 2;
}
if (n==4){
    return 4;
}
if (dp[n]!=-1){
 return dp[n];   
}
    
int pdt=1;
pdt = max(2*recur(n-2),3*recur(n-3));
return dp[n]=pdt;

}
};