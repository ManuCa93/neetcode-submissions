class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diz = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in diz.keys():
                diz[key].append(s)
            else:
                diz[key] = [s]
                
        return list(diz.values())