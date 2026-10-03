class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res

        # we update the boundaries cuz each time a new number is added it only checks its neighbours 
        #Step-by-step with num = 5, and say there's already a streak [3,4] to the left (length 2) and a streak [6,7] to the right (length 2):

#mp[num] = mp[num - 1] + mp[num + 1] + 1

#mp[4] = 2 (left streak length), mp[6] = 2 (right streak length).
#So mp[5] = 2 + 2 + 1 = 5 — the new merged streak [3,4,5,6,7] has length 5. Good, mp[5] is correct.


#mp[num - mp[num - 1]] = mp[num]

#num - mp[num-1] = 5 - 2 = 3 — that's the smallest number of the left streak (its far endpoint). We set mp[3] = 5 so that if a future number like 2 comes in and checks mp[3] (its right neighbor), it sees the correct, updated length of the whole merged streak — not the stale old length of 2.

#mp[num + mp[num + 1]] = mp[num]

#num + mp[num+1] = 5 + 2 = 7 — the largest number of the right streak (its far endpoint). We set mp[7] = 5 similarly, so a future number like 8 checking mp[7] sees the correct merged length.

