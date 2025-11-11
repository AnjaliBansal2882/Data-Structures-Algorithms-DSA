"""
Time Complexity: O(2^n) where n is the length of the input array
Space Complexity: O(n) for recursive stack space
"""

class PrintAllSubSequence:
    def power_set(self, nums):
        ans = []
        self._generate(0, [], ans, nums)
        return ans

    def _generate(self, index, curr, ans, nums):
        if index == len(nums):
            ans.append(list(curr))
            return

        # Include current element
        curr.append(nums[index])
        self._generate(index + 1, curr, ans, nums)
        curr.pop()

        # Exclude current element
        self._generate(index + 1, curr, ans, nums)


# Example usage
if __name__ == "__main__":
    solver = PrintAllSubSequence()
    nums = [1, 2, 3]
    print(solver.power_set(nums))
    # Output: [ [1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], [] ]
