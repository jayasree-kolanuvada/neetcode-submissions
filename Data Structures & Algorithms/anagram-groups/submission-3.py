class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord("a")] += 1
            count = tuple(count)
            hashmap[count].append(word)
        return list(hashmap.values())

        