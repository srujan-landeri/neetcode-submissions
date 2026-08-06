class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0
        ed = len(s) - 1

        while st < ed:
            while st < ed and not s[st].isalnum():
                st += 1

            while st < ed and not s[ed].isalnum():
                ed -= 1

            if s[st].lower() != s[ed].lower():
                return False

            st += 1
            ed -= 1

        return True