class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ris = [1] * n

        # ris[i] = prodotto di tutto ciò che sta a sinistra di i
        sx = 1
        for i in range(n):
            ris[i] = sx
            sx *= nums[i]

        # moltiplico per il prodotto di tutto ciò che sta a destra di i
        dx = 1
        for i in range(n - 1, -1, -1):
            ris[i] *= dx
            dx *= nums[i]

        return ris