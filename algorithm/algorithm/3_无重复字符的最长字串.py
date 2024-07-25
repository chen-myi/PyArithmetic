class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # 初始化变量
        # 开始位置
        start = 0
        # 保存中间结果
        hashmap = {}
        # 维护结果
        max_len = 0
        for end in range(len(s)):
            # end最右边的位置，获取最右边的位置的值，看是否在hashmap中存在，不存在给默认值0并加一
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            # 这个表示上一步执行了给默认值为零的操作，所获取的元素在hashmap中并不存在
            if len(hashmap) == end - start + 1:
                # 更新max_len为max_len和end-start+1的最大值
                max_len = max(max_len, end - start + 1)
            # 这一步表示hashmap出现了重复
            while end - start + 1 > len(hashmap):
                # 获取首位置元素
                head = s[start]
                # 将值减一，因为有可能重复
                hashmap[head] -= 1
                # 如果hashmap[head]为零则不是这个位置重复，删除首元素
                if hashmap[head] == 0:
                    del hashmap[head]
                # start加一看是否下一个元素重复
                start += 1
        return max_len