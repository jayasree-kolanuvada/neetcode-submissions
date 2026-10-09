class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) <= 2:
                continue

            new_count = defaultdict(int)
            for num, c in count.items():
                if c > 1: # we do c>1 here because if c=1 we need to remove it so we do not make a new entry for that num in our new dictionary. this helps us eliminate the unwanted numbers according to the voting algorithm.
                    new_count[num] = c - 1
            count = new_count

        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res


        #your in-place version would be:
# in the above solution we use a new dict cuz if we try to delete keys from a dict when we are iterating over it we get an error. instead we could iterate over the keys converted to a list and del keys from dict respectively.

        #for num in nums:
            #count[num] += 1
            #if len(count) <= 2:
                #continue
            #for k in list(count):
                #count[k] -= 1
                #if count[k] == 0:
                    #del count[k]