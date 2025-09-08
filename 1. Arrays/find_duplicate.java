'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
'''

class Solution {
    public int findDuplicate(int[] nums) {
        int n = nums.length;
        int index =0;
        int[] count = new int[n]; 
        Arrays.fill(count,0);
        for(int i=0;i<n;i++)
        {
            index = nums[i];
            if(count[index] == 0)
            count[index] = 1;
            else
            return index; 
        }
        return 0;
    }
}