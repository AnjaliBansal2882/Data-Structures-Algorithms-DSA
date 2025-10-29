class BookAllocationProblem:

    def find_pages(self, nums, m):
        if m > len(nums):
            return -1

        low = self.max_value(nums)
        high = self.total_sum(nums)

        while low <= high:
            number_of_pages = (high + low) // 2

            if self.number_of_students(nums, number_of_pages) > m:
                low = number_of_pages + 1
            else:
                high = number_of_pages - 1

        return low

    def number_of_students(self, nums, number_of_pages):
        student_count = 1
        curr_sum = 0

        for num in nums:
            if curr_sum + num <= number_of_pages:
                curr_sum += num
            else:
                student_count += 1
                curr_sum = num

        return student_count

    def max_value(self, nums):
        return max(nums)

    def total_sum(self, nums):
        return sum(nums)


# Example usage:
if __name__ == "__main__":
    books = [12, 34, 67, 90]
    students = 2
    solver = BookAllocationProblem()
    print(solver.find_pages(books, students))  # Output: 113
