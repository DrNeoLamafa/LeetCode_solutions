class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1

        tmpStr = ""
        searchIndex = 0
        if len(haystack) < len(needle):
            return index
        while searchIndex != len(haystack):
            if tmpStr == needle:
                break
            for i in range(searchIndex, len(haystack)):
                if tmpStr == needle:
                    break
                elif haystack[i] == needle[len(tmpStr)]:
                    if tmpStr == "":
                        index = i
                    tmpStr = tmpStr + haystack[i]

                else:
                    tmpStr = ""
                    index = -1
                    searchIndex += 1
                    break
        return index
            