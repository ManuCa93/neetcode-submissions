class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dizionario con chiave = lettera e valore = n_volte
        # sort per value
        # prendere prime K key

        diz = {}
        for n in nums:
            diz[n] = diz.get(n, 0) + 1

        ordinati = sorted(diz, key=diz.get, reverse=True)
        return ordinati[:k]