class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        incstack = []
        res = [0]*len(temperatures)

        for i in range (len(temperatures)-1,-1,-1):
            while incstack and temperatures[i] >= incstack[-1][0]:
                incstack.pop()
            if not incstack:
                incstack.append((temperatures[i],i))
            else:
                res[i] = incstack[-1][1] - i
                incstack.append((temperatures[i],i))
        return res

       # monotonic stack - a stack in which we store elements in a strictly inc / dec order. if the elements are not in the order we pop them till we find the right position to push our current element.
       # two types - inc and dec
       # usually used to find next maximum , next smaller element, etc.
       # operation runs in linear time since every element is pushed / popped once at max