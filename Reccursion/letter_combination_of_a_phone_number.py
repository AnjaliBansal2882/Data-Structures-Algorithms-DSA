"""
Time Complexity: O(4^n * n) where n is the length of the input digits string
Space Complexity: O(n) for recursive stack space
"""

class LetterCombinationOfAPhoneNumber:
    def letter_combinations(self, digits):
        if not digits:
            return []

        num_to_char_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        ans = []
        self._solve(digits, num_to_char_map, [], ans, 0)
        return ans

    def _solve(self, digits, num_to_char_map, curr, ans, index):
        if index == len(digits):
            ans.append(''.join(curr))
            return

        characters = num_to_char_map[int(digits[index])]

        for ch in characters:
            curr.append(ch)
            self._solve(digits, num_to_char_map, curr, ans, index + 1)
            curr.pop()  # backtrack


# Example usage
if __name__ == "__main__":
    solver = LetterCombinationOfAPhoneNumber()
    digits = "23"
    print(solver.letter_combinations(digits))
    # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
