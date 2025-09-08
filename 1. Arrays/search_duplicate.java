'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean stat = false;
        for(int i=0;i<m;i++)
        {
            if((matrix[i][n-1] >= target)&&(matrix[i][0]<= target))
            {
                for(int j=n-1;j>=0;j--)
                {
                if(matrix[i][j] == target)
                {
                stat = true;
                break;
                }
                else
                stat = false;
                }
            }
            else
            continue;
        }
        return stat;
    }
}

