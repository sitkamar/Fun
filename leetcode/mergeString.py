class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer: str = ""
        i: int = 0
        j: int = 0
        while i < len(word1) and j < len(word2):
            answer += word1[i]
            i += 1
            answer += word2[j]
            j += 1
        return answer + word1[i:] + word2[j:]
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer: str = ""
        i: int = 0
        j: int = 0
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        if str1[:len(str2)] != str2:
            return ""
        for i in range(len(str2),0,-1):
            answer = str2[:i]
            if str1.replace(answer,"") == "" and str2.replace(answer,"") == "":
                return answer
        return ""
        
            
        # ABAB ABABABABABABABABAB
print(Solution().mergeAlternately("abc", "pqr15"))
print(Solution().gcdOfStrings("ABABABABABABABAB", "ABAB"))