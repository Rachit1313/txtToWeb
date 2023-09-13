#!/usr/bin/env python3

import argparse
import os

# Define the tool's version
VERSION = "txtToWeb v0.1"

def process_file(input_file):
    output_file = os.path.join('txtToWeb', os.path.splitext(os.path.basename(input_file))[0] + ".html")

    with open(input_file, "r") as txt_file, open(output_file, "w") as html_file:
        html_file.write("<!doctype html>\n")
        html_file.write("<html lang='en'>\n")
        html_file.write("<head>\n")
        html_file.write("  <meta charset='utf-8'>\n")
        html_file.write(f"  <title>{os.path.basename(input_file)}</title>\n")
        html_file.write("  <meta name='viewport' content='width=device-width, initial-scale=1'>\n")
        html_file.write("</head>\n")
        html_file.write("<body>\n")
        
        paragraphs = txt_file.read().split('\n\n')

        for paragraph in paragraphs:
            html_file.write(f"  <p>{paragraph}</p>\n")

        html_file.write("</body>\n")
        html_file.write("</html>\n")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                process_file(file_path)

def main():
    if not os.path.exists('txtToWeb'):
        os.makedirs('txtToWeb')

    # Remove existing content from 'txtToWeb' folder
    for filename in os.listdir('txtToWeb'):
        file_path = os.path.join('txtToWeb', filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

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
