import unittest
import argparse
from unittest.mock import patch
from txtToWeb import parse_arguments, handle_arguments, execute_conversion,main

class TestTxtToWeb(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(input_path='test.txt', stylesheet=None, lang='en-US', config=None))
    def test_parse_arguments(self, mock_parse_args):
        args = parse_arguments()
        self.assertEqual(args.input_path, 'test.txt')
        self.assertIsNone(args.stylesheet)
        self.assertEqual(args.lang, 'en-US')
        self.assertIsNone(args.config)

    def test_handle_arguments_with_config(self):
        args = argparse.Namespace(input_path='test.txt', stylesheet=None, lang='en-US', config='config.toml')
        with patch('txtToWeb.parse_config', return_value=('style.css', 'en-CA')) as mock_parse_config:
            input_path, stylesheet_url, lang_attribute = handle_arguments(args)
        mock_parse_config.assert_called_once_with('config.toml', None, 'en-US')
        self.assertEqual(input_path, 'test.txt')
        self.assertEqual(stylesheet_url, 'style.css')
        self.assertEqual(lang_attribute, 'en-CA')

    def test_handle_arguments_without_config(self):
        args = argparse.Namespace(input_path='test.txt', stylesheet='style.css', lang='en-US', config=None)
        with patch('txtToWeb.parse_config', return_value=('style.css', 'en-CA')) as mock_parse_config:
            input_path, stylesheet_url, lang_attribute = handle_arguments(args)
        mock_parse_config.assert_not_called()
        self.assertEqual(input_path, 'test.txt')
        self.assertEqual(stylesheet_url, 'style.css')
        self.assertEqual(lang_attribute, 'en-US')

    @patch('os.path.isfile', return_value=False)
    @patch('os.path.isdir', return_value=False)
    @patch('shutil.rmtree')
    @patch('os.makedirs')
    @patch('builtins.print')
    def test_execute_conversion_with_invalid_input(self, mock_print, mock_makedirs, mock_rmtree, mock_isdir, mock_isfile):
        input_path = 'invalid_path'
        stylesheet_url = 'style.css'
        lang_attribute = 'en-US'
        with self.assertRaises(ValueError):
            execute_conversion(input_path, stylesheet_url, lang_attribute)
        mock_isdir.assert_called_once_with(input_path)
        mock_isfile.assert_called_once_with(input_path)
        mock_rmtree.assert_not_called()
        mock_makedirs.assert_not_called()
        mock_print.assert_called_once_with("Invalid input path. Please provide a valid file or folder path.")

    def test_invalid_input_path(self):
        with patch("sys.argv", ["txtToWeb.py", "nonexistent_path"]):
            with self.assertRaises(SystemExit) as cm:
                main()
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
