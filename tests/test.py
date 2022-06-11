import unittest
from balanced_brackets import is_balanced


class Test(unittest.TestCase):
    def test_unbalanced_string(self):
        assert is_balanced("{[(])}") == "NO", "Result should be 'NO'"
        assert is_balanced("{[])}") == "NO", "Result should be 'NO'"
        assert is_balanced("({))}") == "NO", "Result should be 'NO'"

    def test_balanced_string(self):
        assert is_balanced("{([])}()") == "YES", "Result should be 'YES'"
        assert is_balanced("()") == "YES", "Result should be 'YES'"
        assert is_balanced("{}()[]") == "YES", "Result should be 'YES'"

    def test_unbalanced_string_w_unknown_chars_inbetween(self):
        assert is_balanced("{ [  (     ]  ) }") == "NO", "Result should be 'NO'"
        assert is_balanced("{asc[sadf)332}") == "NO", "Result should be 'NO'"
        assert is_balanced("(asdf{asva)cv52)adsf }") == "NO", "Result should be 'NO'"

    def test_balanced_strin_w_unknown_chars_inbetween(self):
        assert is_balanced("{ ( [ ] ) } (  )") == "YES", "Result should be 'YES'"
        assert is_balanced("(sdaf)dsfa12") == "YES", "Result should be 'YES'"
        assert is_balanced("{cavafd}dfasf(12412d)[4535]cacv") == "YES", "Result should be 'YES'"


if __name__ == '__main__':
    unittest.main()
