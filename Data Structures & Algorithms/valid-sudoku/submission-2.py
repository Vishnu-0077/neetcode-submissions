class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_dup(lst):
            babe = set()
            for x in lst:
                if x in babe:
                    return False
                if x=='.':
                    continue
                babe.add(x)
            return True
        
        def check_board(grid):
            babe = set()
            for row in range(3):
                for col in range(3):
                    if grid[row][col] in babe:
                        return False
                    if grid[row][col]=='.':
                        continue
                    babe.add(grid[row][col])
            return True

        #check rows and colums
        for row in range(9):
            if check_dup(board[row]):
                continue
            else:
                return False

        for col in range(9):
            dup_r = []
            for row in range(9):
                dup_r.append(board[row][col])
            if check_dup(dup_r):
                continue
            else:
                return False
        
        #check boxes
        for i in range(0,3,3):
            for j in range(0,3,3):
                grid = []
                for p in board[i:i+3]:
                    grid.append(p[j:j+3])

                if check_board(grid):
                    continue
                else:
                    return False
        return True

                    

        