class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_rows():
            for row in board:
                seen = set()

                for value in row:
                    if value == '.':
                        continue

                    if value in seen:
                        return False
                    
                    seen.add(value)
            
            return True

        def check_columns():
            for col in range(9):

                seen = set()

                for row in range(9):
                    value = board[row][col]

                    if value == '.':
                        continue
                    
                    if value in seen:
                        return False
                    
                    seen.add(value)
            
            return True

        def check_boxes():
            squares = {}

            for r in range(9):
                for c in range(9):
                    value = board[r][c]

                    if value == ".":
                        continue

                    box = (r // 3, c // 3)

                    if box not in squares:
                        squares[box] = set()

                    if value in squares[box]:
                        return False

                    squares[box].add(value)

            return True

        return check_rows() and check_columns() and check_boxes()

                    