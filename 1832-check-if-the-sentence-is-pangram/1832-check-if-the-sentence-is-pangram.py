class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        visited=[0]*26
        for ch in sentence:
            visited[ord(ch) - ord('a')]=1
        for i in range(len(visited)):
            if visited[i]!=1:
                return False
        return True