class SudokuSolver:

    def solveSudoku(self, board):
        # convert board chars to list of lists for easy mutation
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrid = [[set() for _ in range(3)] for _ in range(3)]

        # Populate the sets
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    rows[i].add(val)
                    cols[j].add(val)
                    subgrid[i // 3][j // 3].add(val)

        # Start solving
        self.backtrack(board, rows, cols, subgrid)

    def backtrack(self, board, rows, cols, subgrid):
        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    # try digits 1–9
                    for val in range(1, 10):
                        if self.isEligible(i, j, rows, cols, subgrid, val):

                            board[i][j] = str(val)
                            rows[i].add(val)
                            cols[j].add(val)
                            subgrid[i // 3][j // 3].add(val)

                            # recurse
                            if self.backtrack(board, rows, cols, subgrid):
                                return True

                            # backtrack
                            board[i][j] = '.'
                            rows[i].remove(val)
                            cols[j].remove(val)
                            subgrid[i // 3][j // 3].remove(val)

                    return False  # no valid number found
        return True  # solved

    def isEligible(self, i, j, rows, cols, subgrid, val):
        return (
            val not in rows[i]
            and val not in cols[j]
            and val not in subgrid[i // 3][j // 3]
        )
