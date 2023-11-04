#!/usr/bin/env python3

import argparse
import os
import shutil
from include.config_parser import parse_config
from include.file_parser import process_file, process_folder

# Define the tool's version
VERSION = "txtToWeb v0.1"


def main():
    parser = argparse.ArgumentParser(
        description="txtToWeb - Convert Text to Web Content"
    )
    parser.add_argument("input_path", help="File or folder path to process")
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=VERSION,
        help="Show the tool's version",
    )
    parser.add_argument(
        "--stylesheet",
        "-s",
        help="URL to a CSS stylesheet to be used in the HTML files",
    )
    parser.add_argument(
        "--lang",
        "-l",
        default="en-CA",  # Default language is Canadian English
        help="Language code to be used in the lang attribute on the root element",
    )
    parser.add_argument(
        "--config",
        "-c",
        help="URL to a TOML config file to be used as a config for the HTML files",
    )

    args = parser.parse_args()
    input_path = args.input_path
    stylesheet_url = args.stylesheet
    lang_attribute = args.lang

    if args.config:
        stylesheet_url, lang_attribute = parse_config(
            args.config, stylesheet_url, lang_attribute
        )

    if os.path.isfile(input_path) and (
        input_path.endswith(".txt") or input_path.endswith(".md")
    ):
        if os.path.exists("til"):
            shutil.rmtree("til")
        os.makedirs("til")
        process_file(input_path, stylesheet_url, lang_attribute)
    elif os.path.isdir(input_path):
        process_folder(input_path, stylesheet_url, lang_attribute)
    else:
        print("Invalid input path. Please provide a valid file or folder path.")


if __name__ == "__main__":
    main()
