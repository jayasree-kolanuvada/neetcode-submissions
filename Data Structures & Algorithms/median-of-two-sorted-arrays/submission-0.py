class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median1 = median2 = 0
        mid = (len(nums1)+len(nums2))//2 + 1
        i,j=0,0
        for count in range(mid):
            median2 = median1
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    median1 = nums1[i]
                    i+=1
                else:
                    median1 = nums2[j]
                    j+=1
            elif i < len(nums1):
                median1 = nums1[i]
                i+=1
            else:
                median1 = nums2[j]
                j+=1
        size = len(nums1)+len(nums2)
        if size%2 == 0:
            return (median1 + median2) / 2
        else:
            return median1

        

        