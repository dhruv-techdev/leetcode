"""
3. Longest Substring Without Repeating Characters

Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    solver = Solution()

    # Dictionary of edge cases: {input_string: expected_output}
    test_cases = {
        "": 0,                  # Edge case: Empty string
        "a": 1,                 # Edge case: Single character
        "bbbbb": 1,             # Edge case: All identical characters
        "abcdef": 6,            # Edge case: All unique characters
        "pwwkew": 3,            # Standard case: Substring in the middle/end
        "abcabcbb": 3,          # Standard case: Repeating patterns
        "abba": 2,              # Critical case: Prevents pointer from moving backwards
        " ": 1,                 # Edge case: Single space
        "a b c a": 3,           # Edge case: Spaces mixed with characters
        "!@#$%^&*()": 10,       # Edge case: Symbols/special characters
    }

    print("Running tests...\n" + "-" * 30)
    for s, expected in test_cases.items():
        result = solver.lengthOfLongestSubstring(s)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Input: {repr(s):<12} | Expected: {expected} | Got: {result} -> {status}")
        assert result == expected, f"Failed on input: {repr(s)}"

    print("-" * 30)
    print("All test cases passed successfully!")