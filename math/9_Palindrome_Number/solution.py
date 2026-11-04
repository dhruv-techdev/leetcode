"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2^31 <= x <= 2^31 - 1


Follow up: Could you solve it without converting the integer to a string?
"""

"""
Approach: Reverse Half of the Number

No string conversion. Pop digits off the end of x and push them onto
reversed_half (same pop and push step as 7. Reverse Integer), but stop at
the middle. A palindrome's first half must equal its reversed second half.
Only reversing half also means the number can never overflow.

Math logic:

    reversed_half = reversed_half * 10 + x % 10 -> push last digit of x
    x             = x // 10                    -> drop last digit of x

Stop when x <= reversed_half: at that point half the digits have moved.

    Even number of digits: halves are the same length
        palindrome if x == reversed_half
    Odd number of digits: reversed_half has the extra middle digit
        drop it with // 10, palindrome if x == reversed_half // 10

Early returns:
    x < 0  -> never a palindrome, the '-' has no match on the right
    x ends in 0 (and x != 0) -> the first digit would have to be 0, which
        is impossible. This check is required: without it x = 10 ends with
        x = 0, reversed_half = 1, and 0 == 1 // 10 would wrongly say True.

Walkthrough 1: x = 1221 (even digits)

x      x % 10   reversed_half
1221     1          1
122      2         12
12       -         stop (12 <= 12)

x == reversed_half -> 12 == 12 -> True

Walkthrough 2: x = 12321 (odd digits)

x      x % 10   reversed_half
12321    1          1
1232     2         12
123      3        123
12       -         stop (12 <= 123)

x == reversed_half // 10 -> 12 == 123 // 10 = 12 -> True

Complexity: Time O(log10 x) (half the digits), Space O(1)
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Move digits from the end of x until the middle is reached
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        # Even digits: halves match. Odd digits: drop the middle digit.
        return x == reversed_half or x == reversed_half // 10

if __name__ == "__main__":

    # Dictionary of edge cases: name -> (x, expected)
    test_cases = {
        "example_1": (121, True),
        "example_2_negative": (-121, False),
        "example_3_trailing_zero": (10, False),
        "zero": (0, True),
        "single_digit": (7, True),
        "two_same_digits": (11, True),
        "even_palindrome": (1221, True),
        "odd_palindrome": (12321, True),
        "not_palindrome": (123, False),
        "zeros_in_middle": (1001, True),
        "trailing_zeros": (100, False),
        "almost_palindrome": (1000021, False),
        "large_palindrome": (1000000001, True),
        "max_int": (2**31 - 1, False),
        "min_int": (-2**31, False),
    }

    print("Running test...\n" + "-" * 30)
    for name, (x, expected) in test_cases.items():
        result = Solution().isPalindrome(x)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Input: {x:<12} | Expected: {str(expected):<6} | Got: {str(result):<6} -> {status}")
        assert result == expected, f"Failed on {name}: {x}"

    print("-" * 30)
    print("All tests completed.")
