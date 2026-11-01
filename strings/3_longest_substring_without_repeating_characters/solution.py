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

"""
Approach: Sliding Window + Hash Map

Keep a window s[left..right] that never contains a repeated character.
char_map remembers the last index where each character was seen.

Math logic:

Window length = right - left + 1

When s[right] was last seen at index p:
    If p >= left  -> the repeat is inside the window, so jump: left = p + 1
    If p <  left  -> the old copy is already outside the window, ignore it
                     (this is why "abba" needs the >= left check, otherwise
                     left would move backwards)

max_len = max(max_len, right - left + 1)

Walkthrough: s = "abcabcbb"

right  char  last seen  left  window   length
  0     a       -        0    a          1
  1     b       -        0    ab         2
  2     c       -        0    abc        3
  3     a       0        1    bca        3
  4     b       1        2    cab        3
  5     c       2        3    abc        3
  6     b       4        5    cb         2
  7     b       6        7    b          1

Answer = 3

Complexity: Time O(n) (each index visited once), Space O(k) where k = number of distinct characters
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