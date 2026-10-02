class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        for i in range(m):
            write = n - 1

            for j in range(n - 1, -1, -1):

                if boxGrid[i][j] == '*':
                    write = j - 1

                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][write] = '#'
                    write -= 1
        result = [[None for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = boxGrid[i][j]

        return result