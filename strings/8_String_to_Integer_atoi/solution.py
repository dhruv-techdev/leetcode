"""
8. String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
Return the integer as the final result.

Note: You must not use any built-in library function that converts a string to a number (for example, atoi, stoi, Integer.parseInt, int(), parseInt, Number()). Perform the conversion manually.



Example 1:

Input: s = "42"
Output: 42
Explanation:
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:

Input: s = "   -042"
Output: -42
Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^
Example 3:

Input: s = "1337c0d3"
Output: 1337
Explanation:
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:

Input: s = "0-1"
Output: 0
Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:

Input: s = "words and 987"
Output: 0
Explanation:
Reading stops at the first non-digit character 'w'.



Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0 - 9), ' ', '+', '-', and '.'.
"""

"""
Approach: Single Pass Parser

Move one index i through the string in three phases, exactly matching the
rules in the problem:
    1. Skip leading spaces
    2. Read an optional '+' or '-' (only one sign is allowed)
    3. Read digits until the first non-digit, then stop

Math logic:

Character to digit without int():
    digit = ord(s[i]) - ord('0')
    '0' is 48 in ASCII and the digits are consecutive, so
    ord('7') - ord('0') = 55 - 48 = 7

Building the number (same push step as 7. Reverse Integer):
    result = result * 10 + digit

    "042" -> 0 * 10 + 0 = 0 -> 0 * 10 + 4 = 4 -> 4 * 10 + 2 = 42
    Leading zeros disappear on their own because 0 * 10 = 0.

Clamping to 32-bit (MAX = 2^31 - 1 = 2147483647, MIN = -2^31 = -2147483648):
    result holds the magnitude only, so as soon as result > 2147483647:
        positive -> return  2147483647
        negative -> return -2147483648
    For "-2147483648" the magnitude 2147483648 is > MAX, and clamping to
    MIN gives exactly the right answer.
    Returning early also stops result from growing on very long inputs.

Walkthrough: s = "   -042"

phase       i   s[i]   action                      sign   result
spaces     0-2   ' '   skip                          1      0
sign        3    '-'   sign = -1                    -1      0
digits      4    '0'   0 * 10 + 0                   -1      0
digits      5    '4'   0 * 10 + 4                   -1      4
digits      6    '2'   4 * 10 + 2                   -1      42
end         7     -    stop

Answer = sign * result = -1 * 42 = -42

Complexity: Time O(n), Space O(1)
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        sign = 1

        i = 0
        n = len(s)
        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Read an optional sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Read digits until the first non-digit
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            if result > 2147483647:
                return 2147483647 if sign == 1 else -2147483648
            i += 1

        return sign * result

if __name__ == "__main__":

    # Dictionary of edge cases: name -> (s, expected)
    test_cases = {
        "example_1": ("42", 42),
        "example_2": ("   -042", -42),
        "example_3": ("1337c0d3", 1337),
        "example_4": ("0-1", 0),
        "example_5": ("words and 987", 0),
        "empty_string": ("", 0),
        "only_spaces": ("   ", 0),
        "only_sign": ("-", 0),
        "plus_sign": ("+1", 1),
        "double_sign": ("+-12", 0),
        "space_after_sign": ("- 12", 0),
        "decimal_point": ("3.14159", 3),
        "leading_zeros": ("  0000000000012345678", 12345678),
        "max_int": ("2147483647", 2147483647),
        "min_int": ("-2147483648", -2147483648),
        "above_max": ("2147483648", 2147483647),
        "below_min": ("-2147483649", -2147483648),
        "huge_number": ("91283472332", 2147483647),
    }

    print("Running test...\n" + "-" * 30)
    for name, (s, expected) in test_cases.items():
        result = Solution().myAtoi(s)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Input: {repr(s):<24} | Expected: {expected:<12} | Got: {result:<12} -> {status}")
        assert result == expected, f"Failed on {name}: {repr(s)}"

    print("-" * 30)
    print("All tests completed.")
