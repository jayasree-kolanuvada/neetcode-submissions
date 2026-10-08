class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
        buckets = [[] for _ in range(len(nums)+1)]
        for val, count in freq.items():
            buckets[count].append(val)
        ans = []
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                if len(ans) == k:
                    return ans
                ans.append(j)
        return ans
        
        