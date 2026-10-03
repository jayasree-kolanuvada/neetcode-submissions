class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l # l always tracks insert position

    # This is just a safer way to compute the midpoint — mathematically it's the same as (l + r) / 2, but written to avoid a classic bug.

#Why not just m = (l + r) / 2?

#In languages with fixed-size integers (like Java, C++), if l and r are both large, l + r can overflow the integer type before the division even happens. For example, if l and r are both near Integer.MAX_VALUE, adding them directly could wrap around to a negative number, giving you a garbage midpoint.

#How l + (r - l) / 2 avoids this
#r - l is the distance between the two pointers — always a small, non-negative number (much smaller than l or r individually), so it can't overflow.
#You take half that distance and add it to l.
#This lands you at exactly the same midpoint as (l + r) / 2 would, but without ever computing a potentially-overflowing sum like l + r.