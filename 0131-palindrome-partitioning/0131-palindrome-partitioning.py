class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current = []

        def solve(start):
            # We reached the end
            if start == len(s):
                result.append(current.copy())
                return

            
            for end in range(start, len(s)):

                if s[start:end+1] == s[start:end+1][::-1]:

                   
                    current.append(s[start:end+1])

                 
                    solve(end + 1)

                
                    current.pop()

        solve(0)
        return result