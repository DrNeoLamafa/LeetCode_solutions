class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(lambda x: int(x) ,str(int(''.join(map(lambda x: str(x), digits))) + 1)))