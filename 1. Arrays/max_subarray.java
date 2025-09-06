'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
'''

class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int sum = 0;
        int max = Integer.MIN_VALUE;
        for(int i=0;i<n;i++)
        {
            sum = 0;
            for(int j=i;j<n;j++)
            {
                sum = sum + nums[j];
                max = Math.max(max,sum); 
            }
           
        }
        return max;
    }
}