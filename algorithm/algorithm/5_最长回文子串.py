class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 定义一个最长回文子串为空字符串
        res = ''
        # 开始遍历
        for i in range(len(s)):
            # 定位开始位置，减去回文子串的长度
            start = max(0, i - len(res) - 1)
            # 确定回文子串
            temp = s[start:i + 1]
            # 反转字符串
            if temp == temp[::-1]:
                res = temp
            else:
                # 去掉首字符
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp

        return res
Solution().longestPalindrome("babab")