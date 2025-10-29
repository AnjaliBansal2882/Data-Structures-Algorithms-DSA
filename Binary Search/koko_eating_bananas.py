class KokoEatingBananas:
    def minimum_rate_to_eat_bananas(self, piles, h):
        low = 1
        high = max(piles)

        while low <= high:
            current_rate = (low + high) // 2
            hours_to_consume = 0

            # Calculate total hours required at current_rate
            for bananas in piles:
                hours_to_consume += bananas // current_rate
                if bananas % current_rate > 0:
                    hours_to_consume += 1  # need one more hour for leftover

            if hours_to_consume > h:
                low = current_rate + 1
            else:
                high = current_rate - 1

        return low


# Example usage:
if __name__ == "__main__":
    koko = KokoEatingBananas()
    piles = [3, 6, 7, 11]
    h = 8
    print(koko.minimum_rate_to_eat_bananas(piles, h))  # Output: 4
