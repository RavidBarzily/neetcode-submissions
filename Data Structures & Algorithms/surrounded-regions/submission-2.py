from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        safe = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i - 1 < 0 or j - 1 < 0 or i + 1 == len(board) or j + 1 == len(board[0])):
                    queue.append((i,j))
                    safe.add((i,j))
        while queue:
            r,c = queue.popleft()
            for dr,dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O" and (nr,nc) not in safe:
                    safe.add((nr,nc))
                    queue.append((nr,nc))

        for i in range(len(board)):
            for j in range(len(board[0])):                
               if board[i][j] == "O" and (i,j) not in safe:
                    board[i][j] = "X"


        