class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            res = 0
            hashMap = {}
            pointer_left, pointer_right = 0, 0
            while pointer_left < len(s) and pointer_right < len(s):
                if s[pointer_right] not in hashMap:
                    hashMap[s[pointer_right]] = 1
                else:
                    res = max(res, len(hashMap.keys()))
                    while s[pointer_left] != s[pointer_right]:
                        del hashMap[s[pointer_left]]
                        pointer_left += 1
                    hashMap[s[pointer_right]] = 1
                    pointer_left += 1
                pointer_right += 1
            return max(res, len(hashMap.keys()))