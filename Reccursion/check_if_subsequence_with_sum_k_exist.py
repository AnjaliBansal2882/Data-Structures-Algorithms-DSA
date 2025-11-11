"""
Time Complexity: O(2^n) where n is the number of elements in the array
Space Complexity: O(n) for recursive stack space
"""

class CheckIfSubSequenceWithSumKExist:
    def check_subsequence_sum(self, nums, k):
        return self._generate(0, 0, nums, k)

    def _generate(self, index, curr_sum, nums, k):
        if k == 0:
            return True

        if k < 0:
            return False

        if index == len(nums):
            return False

        # Include current element
        with_current = self._generate(index + 1, curr_sum + nums[index], nums, k - nums[index])

        # Exclude current element
        without_current = self._generate(index + 1, curr_sum, nums, k)

        return with_current or without_current


# Example usage
if __name__ == "__main__":
    checker = CheckIfSubSequenceWithSumKExist()
    nums = [1, 2, 3]
    k = 5
    print(checker.check_subsequence_sum(nums, k))  # Output: True (2 + 3 = 5)
