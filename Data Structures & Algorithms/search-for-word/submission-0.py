class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, k, visited):
            # k: index in word we’re trying to match
            if k == len(word):
                return True

            # out of bounds?
            if not (0 <= i < rows and 0 <= j < cols):
                return False

            # already used this cell in current path?
            if (i, j) in visited:
                return False

            # character mismatch
            if board[i][j] != word[k]:
                return False

            # mark visited
            visited.add((i, j))

            # explore 4 directions
            found = (
                dfs(i+1, j, k+1, visited) or
                dfs(i-1, j, k+1, visited) or
                dfs(i, j+1, k+1, visited) or
                dfs(i, j-1, k+1, visited)
            )

            # backtrack
            visited.remove((i, j))
            return found

        # try starting from every cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0, set()):
                    return True
        return False
