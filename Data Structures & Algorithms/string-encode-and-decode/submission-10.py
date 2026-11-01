class Solution:

    def encode(self, strs: List[str]) -> str:
        l = ""
        for s in strs:
            l+=(s+"é")
        return l

    def decode(self, s: str) -> List[str]:
        if len(s) > 0:
            return s[:-1].split("é")
        else:
            return []

