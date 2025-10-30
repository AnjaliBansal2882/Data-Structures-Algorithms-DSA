class PaintersPartition:
    MOD = 10000003

    def paint(self, A, B, C):
        low = self.get_max_value(C)
        high = self.get_total_sum(C)

        while low <= high:
            max_sum = (low + high) // 2

            if self.get_max_possible_subarray(C, max_sum) > A:
                low = max_sum + 1
            else:
                high = max_sum - 1

        return (low * B) % self.MOD

    def get_max_possible_subarray(self, arr, max_sum):
        max_subarray = 1
        curr_sum = 0

        for length in arr:
            if curr_sum + length <= max_sum:
                curr_sum += length
            else:
                max_subarray += 1
                curr_sum = length

        return max_subarray

    def get_max_value(self, arr):
        return max(arr)

    def get_total_sum(self, arr):
        return sum(arr)
