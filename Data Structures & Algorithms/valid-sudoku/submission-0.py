class Solution:

    def getDup(self, values):
        values = [x for x in values if x != '.']
        return len(values) == len(set(values))

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check all rows
        for i in range(9):
            if not self.getDup(board[i]):
                return False

        # Check all columns
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if not self.getDup(column):
                return False

        # Check all 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                box = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        box.append(board[i][j])

                if not self.getDup(box):
                    return False

        return True