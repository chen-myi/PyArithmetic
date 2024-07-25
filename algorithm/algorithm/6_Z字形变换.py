class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ["" for _ in range(numRows)]

        i = 0
        flog = -1
        for word in s:
            res[i] += word
            if i == 0 or i == numRows - 1:
                flog = -flog
            i += flog
        return "".join(res)
