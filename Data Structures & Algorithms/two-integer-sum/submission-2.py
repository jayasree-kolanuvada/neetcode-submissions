class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, j in enumerate(nums):
            A.append([j,i])

        A.sort(key=lambda x:x[0])
        left = 0
        right = len(nums)-1
        while left<right:
            curr = A[left][0] + A[right][0]
            if curr == target:
                return [min(A[left][1], A[right][1]), max(A[left][1], A[right][1])]
            elif curr > target:
                right-=1
            else:
                left+=1
        