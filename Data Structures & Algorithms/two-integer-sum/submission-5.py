class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = list()
        for i , num in enumerate(nums):
            A.append((i,num))

        A.sort(key=lambda x:x[1])
        left = 0
        right = len(nums) - 1

        while left < right:
            if A[left][1] + A[right][1] == target:
                return [min(A[left][0], A[right][0]), max(A[left][0],A[right][0])]

            elif A[left][1] + A[right][1] > target:
                right-=1

            if A[left][1] + A[right][1] < target:
                left+=1
