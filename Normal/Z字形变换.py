class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        1 1
        2 2
        3 4
        4 6
        5 8
        """
        str_by_line = ['' for _ in range(numRows)]
        if numRows == 1:
            return s
        else:
            for i,c in enumerate(s):
                loc = i % ((numRows-1)*2)
                if loc // numRows :
                    str_by_line[numRows - 2 - loc % numRows] += c
                else:
                    str_by_line[loc] += c
        msg = ""
        for string in str_by_line:
            msg +=string
        return msg