'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        pct = [[1],[1,1]]
        if numRows < 3:
            return pct[:numRows]
        else:
            for i in range(2,numRows):
                pct.append([1])
                for j in range(1,i):
                    pct[i].append(pct[i-1][j-1] + pct[i-1][j])
                pct[i].append(1)
        return pct

 

        