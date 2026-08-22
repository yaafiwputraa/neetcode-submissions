class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n  # Inisialisasi hasil dengan 1

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]  # Hitung prefix product

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]  # Hitung suffix product

        return res