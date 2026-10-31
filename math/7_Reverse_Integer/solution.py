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
