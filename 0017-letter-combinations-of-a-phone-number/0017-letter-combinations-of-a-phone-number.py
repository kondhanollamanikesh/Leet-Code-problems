class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': []
        }
        result=[]
        def solve(ind,subset):
            if len(subset)==len(digits):
                result.append("".join(subset.copy()))
                return
            if ind>=len(digits):
                return
            if not digits:
                return []
            for ch in keypad[digits[ind]]:
                subset.append(ch)
                solve(ind+1,subset)
                subset.pop()
        solve(0,[])
        return result