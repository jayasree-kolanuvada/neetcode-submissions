class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num,0)+1
        buckets = [[]for _ in range (len(nums)+1)]
        for num, freq in freq.items():
            buckets[freq].append(num)

        ans = []
        for i in range (len(buckets)-1,0,-1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans
        return ans
        
        
        