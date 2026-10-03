class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num,0)+1
        data = list(frequency.items())
        data.sort(key = lambda x:x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(data[i][0])

        return ans
        