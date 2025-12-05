class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        numOfEvenPartitions = 0
        isRightOdd = sum(nums) & 1
        isLeftOdd = 0 # init to 0, XOR will set this to even or odd properly on the first run
        for i in range(len(nums) - 1):
            isCurrentOdd = nums[i] & 1
            isRightOdd ^= isCurrentOdd
            isLeftOdd ^= isCurrentOdd
            if isLeftOdd == isRightOdd:
                numOfEvenPartitions += 1

        return numOfEvenPartitions
