"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        rom_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        r_int = 0
        for i in range(len(s)):
            num = rom_dict[s[i]]
            if i != 0:
                pre_num = rom_dict[s[i-1]]
            else:
                pre_num = 0
            
            if pre_num < num:
                r_int += num - pre_num * 2
            else:
                r_int += num
        return r_int
        
if __name__ == "__main__":
    s = 'MCMXCIV'
    sol = Solution()
    result = sol.romanToInt(s)
    print(result)


"""
Short solution

class Solution:
    def romanToInt(self, s: str) -> int:
        my_list = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        my_num = []
        for num in s:
            if my_num != [] and my_list[num] > my_num[-1]:
                my_num[-1] = my_list[num] - my_num[-1]
            else:
                my_num.append(my_list[num])
        return sum(my_num)
"""
