# Last updated: 23/07/2026, 15:08:31


class Solution(object):
    def groupAnagrams(self, strs):
        out= defaultdict(list)
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            key=tuple(count)
            out[key].append(i)
        return out.values()

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        