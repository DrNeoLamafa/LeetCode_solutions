class Solution:
    def divOrNot(self, i):
        if (i % 3 == 0 and i % 5 == 0):
            return "FizzBuzz"
        elif(i % 3 == 0):
            return "Fizz"
        elif (i % 5 == 0):
            return "Buzz"
        else:
            return f"{i}"
        
    def fizzBuzz(self, n: int) -> List[str]:
        
        result = tuple( self.divOrNot(i) for i in range(1, n+1))
        return result
    
    