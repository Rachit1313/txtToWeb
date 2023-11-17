import unittest
from your_module import md_to_html  # Replace 'your_module' with the actual module name containing md_to_html

class TestMdToHtml(unittest.TestCase):

    def test_italic_conversion(self):
        input_text = "This is *italic* text."
        expected_output = "This is <i>italic</i> text."
        self.assertEqual(md_to_html(input_text), expected_output)

    def test_horizontal_rule_conversion(self):
        input_text = "Some text\n---\nMore text"
        expected_output = "Some text\n<hr>\nMore text"
        self.assertEqual(md_to_html(input_text), expected_output)

    def test_no_conversion(self):
        input_text = "This is plain text."
        self.assertEqual(md_to_html(input_text), input_text)

if __name__ == '__main__':
    unittest.main()
