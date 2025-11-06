class GenerateParentheses:
    def generate_parenthesis(self, n):
        result = []
        self._generate("", 0, 0, n, result)
        return result

    def _generate(self, current, open_count, close_count, n, result):
        # Base case: when the string has 2*n characters
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add '(' if we still have open brackets left to add
        if open_count < n:
            self._generate(current + "(", open_count + 1, close_count, n, result)

        # Add ')' only if it won’t make the sequence invalid
        if close_count < open_count:
            self._generate(current + ")", open_count, close_count + 1, n, result)
