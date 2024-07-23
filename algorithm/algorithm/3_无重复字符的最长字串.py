class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        hashmap = {}
        max_len = 0
        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if len(hashmap) == end - start + 1:
                max_len = max(max_len,end - start + 1)
            while end - start + 1 > len(hashmap):
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        return max_len