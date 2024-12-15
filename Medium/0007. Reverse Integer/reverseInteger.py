class Solution:
    def reverse(self, x: int) -> int:
        tmp = str(x)
        if x >= 0:
            tmp = tmp[::-1]   
        else:
            tmp = '-' + tmp[:-len(tmp):-1]
            #tmp = tmp[::-1]
        tmp = int(tmp)
        
        if tmp.bit_length() >= 32:
            return 0
        else:
            return tmp
            