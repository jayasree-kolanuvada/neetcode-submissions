class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res


[-4, -1, -1, 0, 1, 2]
# leaving count of nums[j] decremented is intentional, and it’s what makes this version correct.
# As `j` moves forward, `count` only holds the elements at indices after `j`. Every element at index ≤ `j` has already been subtracted. So `count[target] > 0` means “target exists somewhere to the right of `j`”. That gives you `i < j < k` for every triplet, which does two things:
#
# 1. No element is reused. The third number can never be `nums[i]` or `nums[j]` itself.
# 2. Each triplet is found only once. The third number always comes from the right.
#
# If you restored `count[nums[j]]` inside the inner loop, the third number could come from the left of `j`. With `[-1, 0, 1]`, you’d find:
#
# * `i=-1, j=0`, target `1` (to the right of `j`): correct.
# * `i=-1, j=1`, target `0`: `0` sits to the left of `j`, but its count was restored, so it’s found again. That gives a duplicate `[-1, 1, 0]`.
#
# The same logic applies to `count[nums[i]]`, which is never restored. Once `i` moves on, earlier elements shouldn’t be usable anymore.
        
        