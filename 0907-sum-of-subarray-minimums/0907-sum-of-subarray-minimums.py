# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        A = [0]+A
        res =[0]*len(A)
        st =[0] # we push indices into stack
        
        for i in range(len(A)):
            while A[st[-1]]>A[i]:
                st.pop()
            
            j= st[-1]
            # print(i,j)
            res[i] = res[j]+(i-j)*A[i]
            st.append(i)
        # print(res)
        return sum(res)%(10**9+7)