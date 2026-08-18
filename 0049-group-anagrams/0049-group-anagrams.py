class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        res=[]
        for key,value in groups.items():
            res.append(value)


        return res    