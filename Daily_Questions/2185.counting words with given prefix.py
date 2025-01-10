class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a=len(pref)
        count=0
        for i in range(len(words)):
            if words[i][0:a] == pref:
                count+=1
        return count
