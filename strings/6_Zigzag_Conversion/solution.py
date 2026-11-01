"""
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

"""
Approach: Simulate the Zigzag Row by Row

Instead of drawing the 2D grid, keep one list per row and drop each
character into the row it would land in. Reading the zigzag line by line
is then just joining the rows top to bottom.

Math logic:

The row index moves down then up, bouncing between 0 and numRows - 1:
    0, 1, 2, ..., numRows - 1, numRows - 2, ..., 1, 0, 1, 2, ...

direction = +1 while going down, -1 while going up
    At row 0           -> direction = +1
    At row numRows - 1 -> direction = -1
    current_row = current_row + direction

The pattern repeats every 2 * (numRows - 1) characters.

Edge cases:
    numRows == 1        -> no zigzag, the string stays the same
    numRows >= len(s)   -> every character gets its own row, so the
                           string stays the same

Walkthrough: s = "PAYPALISHIRING", numRows = 3

char:  P A Y P A L I S H I R I N G
row:   0 1 2 1 0 1 2 1 0 1 2 1 0 1

Row 0: P A H N
Row 1: A P L S I I G
Row 2: Y I R

Answer = "PAHN" + "APLSIIG" + "YIR" = "PAHNAPLSIIGYIR"

Complexity: Time O(n), Space O(n)
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row].append(char)

            # Bounce off the top and bottom rows
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join("".join(row) for row in rows)

if __name__ == "__main__":

    # Dictionary of edge cases: name -> (s, numRows, expected)
    test_cases = {
        "example_3_rows": ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        "example_4_rows": ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        "single_char": ("A", 1, "A"),
        "one_row": ("ABCDEF", 1, "ABCDEF"),
        "two_rows": ("ABCDEF", 2, "ACEBDF"),
        "rows_equal_length": ("ABCD", 4, "ABCD"),
        "rows_exceed_length": ("AB", 5, "AB"),
        "with_punctuation": ("a,b.c", 2, "abc,."),
    }

    print("Running test...\n" + "-" * 30)
    for name, (s, num_rows, expected) in test_cases.items():
        result = Solution().convert(s, num_rows)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Input: {repr(s):<18} rows={num_rows:<2} | Expected: {expected:<16} | Got: {result:<16} -> {status}")
        assert result == expected, f"Failed on {name}: {repr(s)}, numRows={num_rows}"

    print("-" * 30)
    print("All tests completed.")
