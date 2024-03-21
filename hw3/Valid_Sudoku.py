class Solution(object):
    def isValidSudoku(self, board):
        seen=set()

        for r in range(9):
            for c in range(9):
                if board[r][c]!='.':
                    val=board[r][c]

                    rk=(val,'in row',r)
                    ck=(val,'in column',c)
                    bk=(val,'in box',r//3,c//3)

                    if((rk in seen) or (ck in seen) or (bk in seen)):
                        return False
                        
                    seen.add(rk)
                    seen.add(ck)
                    seen.add(bk)
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        