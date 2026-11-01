"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-2^31 <= x <= 2^31 - 1
"""

"""
Approach: Pop and Push Digits

Repeatedly pop the last digit off x and push it onto the end of result.
The sign is handled separately: work with abs(x), then multiply the sign
back at the end. (In Python, -123 % 10 = 7, not -3, so working with
negative numbers directly would give wrong digits.)

Math logic:

    digit  = x % 10              -> last digit of x
    x      = x // 10             -> drop the last digit from x
    result = result * 10 + digit -> append digit to the end of result

Overflow check (32-bit max is 2^31 - 1 = 2147483647):

    result * 10 + digit overflows when result > 2147483647 // 10 = 214748364
    So check result > 214748364 before multiplying.

    The case result == 214748364 with digit > 7 can't happen: x would need
    10 digits starting with 8 or 9, which is already bigger than 2^31.

Walkthrough: x = 123

x     digit = x % 10   result = result * 10 + digit   x = x // 10
123        3                0 * 10 + 3 = 3                 12
12         2                3 * 10 + 2 = 32                1
1          1               32 * 10 + 1 = 321               0

Answer = 321 * sign

Trailing zeros disappear on their own: x = 120 -> result goes 0, 2, 21

Complexity: Time O(log10 x) (one loop per digit, at most 10), Space O(1)
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        result = 0

        while x != 0:
            digit = x % 10
            # Stop before result * 10 can exceed the 32-bit limit
            if result > (2**31 - 1) // 10:
                return 0
            result = result * 10 + digit
            x = x // 10

        return result * sign

if __name__ == "__main__":

    # Dictionary of edge cases: name -> (x, expected)
    test_cases = {
        "positive": (123, 321),
        "negative": (-123, -321),
        "trailing_zero": (120, 21),
        "zero": (0, 0),
        "single_digit": (7, 7),
        "negative_single_digit": (-8, -8),
        "max_int_overflow": (2**31 - 1, 0),
        "min_int_overflow": (-2**31, 0),
        "overflow": (1534236469, 0),
        "near_max_no_overflow": (1463847412, 2147483641),
        "near_min_no_overflow": (-1463847412, -2147483641),
    }

    print("Running test...\n" + "-" * 30)
    for name, (x, expected) in test_cases.items():
        result = Solution().reverse(x)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Input: {x:<12} | Expected: {expected:<12} | Got: {result:<12} -> {status}")
        assert result == expected, f"Failed on {name}: {x}"

    print("-" * 30)
    print("All tests completed.")
