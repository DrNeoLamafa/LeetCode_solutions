class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):

            tempRow = [item for item in board[i] if item != '.']
            
            
            tempCol = [ item[i] for item in board if item[i] != '.']
            
            if len(tempCol) != len(set(tempCol)) or len(tempRow) != len(set(tempRow)):
                return False
        
        
        for st in range(3, 11, 3):
                for col in range(3, 11, 3):
                      tempCube = [item for l in board[st-3:st]  for item in l[col-3:col] if item != '.']  
                      if len(tempCube) != len(set(tempCube)):
                            return False
        return True