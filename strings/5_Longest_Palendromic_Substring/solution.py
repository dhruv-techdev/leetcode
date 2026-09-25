"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s
            
        def expand_around_center(left, right):
            # Expand outwards as long as the characters match and are within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1
            
        start = 0
        end = 0
        
        for i in range(len(s)):
            # Odd length palindromes (e.g., "aba") with center at i
            len1 = expand_around_center(i, i)
            # Even length palindromes (e.g., "abba") with center between i and i+1
            len2 = expand_around_center(i, i + 1)
            
            # Find the max length from both expansions
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update the start and end pointers
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        # Return the substring from start to end (inclusive)
        return s[start:end + 1]

if __name__ == "__main__":

    def is_palindrome(text):
        return text == text[::-1]

    # Dictionary of edge cases. For ambiguous cases like "babad", either
    # "bab" or "aba" is valid, so we check the result is a palindrome and
    # matches the correct length instead of requiring one exact string.
    test_cases = {
        "single_char": ("a", "a"),
        "odd_palindrome": ("babad", "bab"),
        "even_palindrome": ("cbbd", "bb"),
        "all_same": ("aaaa", "aaaa"),
        "mixed_case": ("abacdfgdcaba", "aba"),
        "no_palindrome": ("abcde", "a"),
        "two_chars": ("bb", "bb"),
        "empty_string": ("", "")
    }

    print("Running test...\n" + "-" * 30)
    for name, (s, expected) in test_cases.items():
        result = Solution().longestPalindrome(s)
        is_valid = is_palindrome(result) and len(result) == len(expected) and result in s if s else result == ""
        status = "PASSED" if is_valid else "FAILED"
        print(f"Input: {repr(s):<12} | Expected: {expected} | Got: {result} -> {status}")
        assert is_valid, f"Failed on input: {repr(s)}"

    print("-" * 30)
    print("All tests completed.")
    