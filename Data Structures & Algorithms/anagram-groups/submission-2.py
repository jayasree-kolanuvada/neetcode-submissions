class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        ans = []
        for str in strs:
            sorted_str = "".join(sorted(str))
            mydict[sorted_str].append(str)
        for k,v in mydict.items():
            ans.append(v)
        return ans

     