class AggressiveCows:
    def aggressive_cows(self, stalls, k):
        stalls.sort()

        low = 1
        high = stalls[-1] - stalls[0]  # max possible distance

        while low <= high:
            min_distance = (low + high) // 2
            cows_placed = self._count_cows(stalls, min_distance)

            if cows_placed >= k:
                low = min_distance + 1  # try for larger distance
            else:
                high = min_distance - 1  # reduce distance

        return low - 1  # last valid distance

    def _count_cows(self, stalls, min_distance):
        cows_placed = 1
        last_position = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= min_distance:
                cows_placed += 1
                last_position = stalls[i]

        return cows_placed


# Example usage:
if __name__ == "__main__":
    cows = AggressiveCows()
    stalls = [1, 2, 8, 4, 9]
    k = 3
    print(cows.aggressive_cows(stalls, k))  # Output: 3
