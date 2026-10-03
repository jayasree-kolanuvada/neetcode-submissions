class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse = True)
        if h == len(piles):
            return piles[0]
        l = 1
        hi = piles[0]
        res = float("inf")
        while l <= hi:
            m = l + (hi-l)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/m)
            if hours > h:
                l = m+1
            elif hours <= h:
                res = min(res,m)
                hi = m-1
        return res


            




