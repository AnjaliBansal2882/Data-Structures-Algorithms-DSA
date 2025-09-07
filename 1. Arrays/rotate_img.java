'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int[][] rotate = new int[n][n];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                rotate[j][n-1-i] = matrix[i][j];
            }
        }
        for(int i=0;i<n;i++)
        {
        System.arraycopy(rotate[i],0, matrix[i],0,n);
        }
    }
}