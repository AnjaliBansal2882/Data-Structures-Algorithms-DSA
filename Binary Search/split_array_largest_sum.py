class SplitArrayLargestSum:

    def largest_subarray_sum_minimized(self, arr, k):
        low = self.get_max_value(arr)
        high = self.get_total_sum(arr)

        while low <= high:
            max_sum = (low + high) // 2

            if self.get_max_possible_subarray(arr, max_sum) > k:
                low = max_sum + 1
            else:
                high = max_sum - 1

        return low

    def get_max_possible_subarray(self, arr, max_sum):
        subarrays = 1
        curr_sum = 0

        for num in arr:
            if curr_sum + num <= max_sum:
                curr_sum += num
            else:
                subarrays += 1
                curr_sum = num

        return subarrays

    def get_max_value(self, arr):
        return max(arr)

    def get_total_sum(self, arr):
        return sum(arr)


# Example usage:
if __name__ == "__main__":
    solver = SplitArrayLargestSum()
    nums = [7, 2, 5, 10, 8]
    k = 2
    result = solver.largest_subarray_sum_minimized(nums, k)
    print(result)  # Expected output: 18
