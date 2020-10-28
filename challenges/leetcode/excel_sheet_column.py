"""
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""
import unittest


def excel_sheet_column(col):
    rez = 0
    for i in range(len(col)):
        rez += (ord(col[i]) - 64) * pow(26, len(col) - i - 1)

    return rez


class TestExcelSheetColumn(unittest.TestCase):
    def test_excel_sheet_column_A(self):
        self.assertEqual(1, excel_sheet_column('A'))

    def test_excel_sheet_column_AA(self):
        self.assertEqual(27, excel_sheet_column('AA'))

    def test_excel_sheet_column_AAA(self):
        self.assertEqual(703, excel_sheet_column('AAA'))