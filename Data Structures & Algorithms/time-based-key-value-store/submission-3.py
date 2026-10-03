class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)   

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.tmap[key]
        if not values or (values and  timestamp < values[0][1]):
            return ""
        l = 0
        r = len(values)-1
        while l <= r:
            m = (l+r)//2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                r = m-1
            else:
                l = m+1
        return values[l-1][0]
        
