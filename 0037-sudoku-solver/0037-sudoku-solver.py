class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for row in range(9):
            for col in range(9):

                num = board[row][col]

                if num != ".":
                    box = (row // 3) * 3 + (col // 3)

                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

        def solve():

            for row in range(9):
                for col in range(9):

                    if board[row][col] == ".":

                        box = (row // 3) * 3 + (col // 3)

                        for num in "123456789":

                            if (num not in rows[row] and
                                num not in cols[col] and
                                num not in boxes[box]):

                                # Choose
                                board[row][col] = num
                                rows[row].add(num)
                                cols[col].add(num)
                                boxes[box].add(num)

                                # Explore
                                if solve():
                                    return True

                                # Undo
                                board[row][col] = "."
                                rows[row].remove(num)
                                cols[col].remove(num)
                                boxes[box].remove(num)

                        return False

            return True

        solve()