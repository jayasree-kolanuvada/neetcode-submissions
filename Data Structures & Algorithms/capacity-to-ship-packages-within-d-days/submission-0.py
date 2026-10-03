class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            m = l + (r-l)//2
            total_days = 0
            capacity = 0
            i = 0
            while i <=len(weights):
                if capacity > m:
                    total_days += 1
                    capacity = 0
                    i -= 1
                elif capacity == m:
                    total_days += 1
                    capacity = 0
                elif i < len(weights):
                    capacity += weights[i]
                    i+=1
                else:
                    break
            if capacity:
                total_days+=1
            if total_days > days:
                l = m+1
            else:
                res = m
                r = m-1
        return res

        