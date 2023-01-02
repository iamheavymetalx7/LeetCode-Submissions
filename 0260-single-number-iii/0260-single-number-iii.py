class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2=0
        
        for num in nums:
            n1xn2^=num
            
        # print(n1xn2)
            
        rightmost_bit=1
        
        while rightmost_bit & n1xn2 ==0:
            rightmost_bit = rightmost_bit<<1
        # print(rightmost_bit)
        num1,num2=0,0
        
        for num in nums:
            if rightmost_bit & num !=0:
                num1^=num
            else:
                num2^=num
        
        return [num1,num2]