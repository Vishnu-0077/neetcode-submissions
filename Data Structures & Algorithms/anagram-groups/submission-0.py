class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            new1 = ''.join(sorted(list(word)))
            if new1 not in map:
                map[new1]=[word]
            else:
                map[new1].append(word)
        return list(map.values())


