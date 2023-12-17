class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for alphabet in s:
            record[ord(alphabet) - ord("a")] += 1
        for alphabet in t:
            record[ord(alphabet) - ord("a")] -= 1
        for count in record:
            if count != 0:
                return False
        return True
        
"""
Remember the ord(), it's easy to use to get the unicode of alphabet
Set the 26 0 in record to make it as the hash table
If alphabet present in s than +1
If used in t than -1
If != 0 than false
"""