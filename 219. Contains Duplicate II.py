class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #intuition - sliding window keep track of i-j or k window values.
        n = len(nums)
        if n == 1 or k == 0: return False

        l, r = 0, 1
        k_window = set([nums[l]])

        while r <= n - 1:
            if nums[r] in k_window:
                return True
            k_window.add(nums[r])
            if r - l < k:
                r += 1
            else:
                k_window.remove(nums[l])
                l += 1
                r += 1

        return False


        