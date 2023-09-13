#!/usr/bin/env python3

import argparse
import os

# Define the tool's version
VERSION = "txtToWeb v0.1"

def process_file(file_path):
    # Replace this logic with your actual processing code for a single file.
    print(f"Processing file: {file_path}")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_file(file_path)

def main():
    parser = argparse.ArgumentParser(description="txtToWeb - Convert Text to Web Content")
    parser.add_argument("input_path", help="File or folder path to process")
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=VERSION,
        help="Show the tool's version",
    )

    args = parser.parse_args()
    input_path = args.input_path

    if os.path.isfile(input_path):
        process_file(input_path)
    elif os.path.isdir(input_path):
        process_folder(input_path)
    else:
        print("Invalid input path. Please provide a valid file or folder path.")

if __name__ == "__main__":
    main()
