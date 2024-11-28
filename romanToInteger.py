class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        prev = 0
        romans = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum = 0
        prev = 0
        for x in reversed(s):
            value = romans[x]
            if value < prev:
                sum -= value
            else:
                sum += value
            prev = value
        return sum
