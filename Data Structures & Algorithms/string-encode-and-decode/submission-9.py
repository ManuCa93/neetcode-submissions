class Solution:

    def encode(self, strs):
        return "".join(str(len(s)) + "#" + s for s in strs)
    # ["hi", "a#b"] -> "2#hi3#a#b"

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = s.find("#", i)              # the first # after i ends the length
            length = int(s[i:j])            # "3"
            res.append(s[j + 1 : j + 1 + length])   # take exactly `length` characters
            i = j + 1 + length              # jump to the next block
        return res

