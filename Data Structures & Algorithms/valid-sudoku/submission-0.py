class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(9):
            row_set = set()

            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                # Check row
                if value in row_set:
                    return False
                row_set.add(value)

                # Check column
                if value in col_sets[j]:
                    return False
                col_sets[j].add(value)

                # Check 3 × 3 box
                box_index = (i // 3) * 3 + (j // 3)

                if value in box_sets[box_index]:
                    return False
                box_sets[box_index].add(value)

        return True