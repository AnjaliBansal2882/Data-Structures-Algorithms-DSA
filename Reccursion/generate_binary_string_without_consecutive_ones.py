class GenerateBinaryStringWithoutConsecutiveOnes:
    def generate_binary_strings(self, n):
        result = []
        self._generate(n, "", result)
        return result

    def _generate(self, n, s, result):
        if n == 0:
            result.append(s)
            return

        # Always can add '0'
        self._generate(n - 1, s + "0", result)

        # Can add '1' only if last char is not '1'
        if not s or s[-1] != '1':
            self._generate(n - 1, s + "1", result)
