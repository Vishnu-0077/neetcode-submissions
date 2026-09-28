class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(board,x,y,word,c,visited):
            if c==len(word)-1:
                return True
            visited.add((x,y))
    
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            for way in directions:
                i,j = way
                xn = x+i
                yn = y+j
                if 0<=xn<len(board) and 0<=yn<len(board[0]) and (xn,yn) not in visited and  word[c+1]==board[xn][yn]:
                    if search(board,xn,yn,word,c+1,visited):
                        return True
            visited.remove((x,y))
            return False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    visited = set()
                    if search(board,x,y,word,0,visited):
                        return True
        return False

        