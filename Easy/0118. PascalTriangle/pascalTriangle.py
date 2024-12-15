class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resultList = list()
        for rn in range(numRows):
            row = [1]
            
            if rn == 1:
                row.append(1)
            elif rn > 1:
                for i in range(1, rn):
                    row.append(resultList[rn-1][i-1] + resultList[rn-1][i])
                row.append(1)
            resultList.append(row)
        return resultList