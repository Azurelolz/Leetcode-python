"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

class Solution(object):
    def isValid(self, s):
        next_valid_char = ''
        if not s:
            return False
        for char in s:
            if not next_valid_char:
                if char == '(':
                    next_valid_char = ')'
                elif char == '[':
                    next_valid_char = ']'
                elif char == '{':
                    next_valid_char = '}'
                else:
                    next_valid_char = ''
            elif char == next_valid_char:
                next_valid_char = ''
            elif char != next_valid_char:
                return False
        return True

if __name__ == "__main__":
    s = "()[]{}"
    sol = Solution()
    result = sol.isValid(s)
    print(result)

"""
Better solution

class Solution(object):
    def isValid(self, s):
        map = {')':'(', '}':'{', ']':'['}
        st = []
        for e in s:
            if st and (e in map and st[-1] == map[e]):
                st.pop()
            else:
                st.append(e)
        return not st
"""