class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Modify board in-place.
        """
        def find_empty_location(arr, l):
            for row in range(9):
                for col in range(9):
                    if(arr[row][col] == "."):
                        l[0]= row
                        l[1]= col
                        return True
            return False

        def used_in_row(arr, row, num):
            for i in range(9):
                if(arr[row][i] == num):
                    return True
            return False
        
        def used_in_col(arr, col, num):
            for i in range(9):
                if(arr[i][col] == num):
                    return True
            return False
        
        def used_in_box(arr, row, col, num):
            for i in range(3):
                for j in range(3):
                    if(arr[i + row][j + col] == num):
                        return True
            return False
        
        def check_location_is_safe(arr, row, col, num):
            return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num)
        
        def solve_sudoku(arr):
            # 'l' es una variable de tipo lista que mantiene el registro de filas y columnas en find_empty_location  
            l =[0, 0]
        
            if(not find_empty_location(arr, l)):
                return True
            row = l[0]
            col = l[1]
            
            for num in range(1, 10):
                if(check_location_is_safe(arr, row, col, str(num))):
                    arr[row][col]= str(num)

                    if(solve_sudoku(arr)):
                        return True
                    
                    arr[row][col] = "."     
            return False
        solve_sudoku(board)
        return board
######TEST######
Sudoku = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Sudoku.solveSudoku(board)
################