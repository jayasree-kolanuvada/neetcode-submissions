class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        l = 1
        hi = max(piles)
        res = hi #it cannote be more than max size of pile
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


            




