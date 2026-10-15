class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr
        l = 0
        r = len(arr)-1
        while l < r:
            mid = (l+r)//2
            if arr[mid] < x:
                l = mid+1
            else:
                r = mid
        r = l
        l -= 1
        while True:
            if r==len(arr) or l>=0 and abs(arr[l]-x) <= abs(arr[r]-x):
                l -= 1
            elif r<len(arr):
                r += 1
            if (r-l+1) == k+2:
                break
        ans = []
        for i in range(l+1,r):
            ans.append(arr[i])
        return ans
            



        
        