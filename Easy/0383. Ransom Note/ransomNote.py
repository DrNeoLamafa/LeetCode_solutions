class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        eachNote = ""
        while (len(ransomNote) != 0):
            if ransomNote[0] not in magazine:
                return False
            else:
                magazine = magazine.replace(ransomNote[0], "", 1)
                ransomNote = ransomNote.replace(ransomNote[0], "", 1)               
        return True