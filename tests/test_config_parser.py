# test_config_parser.py

import unittest
from include.config_parser import parse_config
from unittest.mock import mock_open, patch


class TestConfigParser(unittest.TestCase):
    def test_parse_valid_config(self):
        mock_file_data = b'[default]\nstylesheet = "style.css"\nlang = "en-US"'
        with patch("builtins.open", mock_open(read_data=mock_file_data)):
            stylesheet_url, lang_attribute = parse_config(
                "config.toml", "default_style.css", "en-US"
            )
            self.assertEqual(stylesheet_url, "default_style.css")
            self.assertEqual(lang_attribute, "en-US")

    # Add more tests for invalid configs, missing values, etc.


if __name__ == "__main__":
    unittest.main()
