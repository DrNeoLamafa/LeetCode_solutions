class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
         
        allNum = [1] * n
        allNum[0], allNum[1] = False, False
        for i in range(2, n):
            if (allNum[i]):
                for j in range(i ** 2, n, i):
                    allNum[j] = False

        result = sum(allNum) 
        return result