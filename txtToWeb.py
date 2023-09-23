#!/usr/bin/env python3

import argparse
import os
import shutil
import re

# Define the tool's version
VERSION = "txtToWeb v0.1"

def md_to_html(content):
    # Convert Markdown italic syntax to HTML
    content = re.sub(r"([*_])([^*_]*)(\1)", r"<i>\2</i>", content)
    return content


def extract_title_and_content(file_path):
    with open(file_path, "r") as txt_file:
        lines = txt_file.readlines()

        title = ""
        content = ""

        if file_path.endswith('.md'):
            content = md_to_html("".join(lines))
        else:
            # Check if there is at least one line in the file
            if lines:
                # Check the first line
                first_line = lines[0].strip()

                # Check the next two lines if they exist
                if len(lines) > 2 and not lines[1].strip() and not lines[2].strip():
                    # If the first line is not empty, consider it a title
                    if first_line:
                        title = first_line
                    # Read the rest of the lines as content
                    content = "".join(lines[3:])
                else:
                    content = "".join(lines)
            else:
                pass

        return title.strip(), content.strip()

def process_file(input_file,stylesheet_url):
    output_file = os.path.join('til', os.path.splitext(os.path.basename(input_file))[0] + ".html")
    title, content = extract_title_and_content(input_file)
    with open(output_file, "w") as html_file:
        html_file.write("<!doctype html>\n")
        html_file.write("<html lang='en'>\n")
        html_file.write("<head>\n")
        html_file.write("  <meta charset='utf-8'>\n")
        if title:
            html_file.write(f"  <title>{title}</title>\n")
        html_file.write("  <meta name='viewport' content='width=device-width, initial-scale=1'>\n")
        if stylesheet_url:
            html_file.write(f"  <link rel='stylesheet' type='text/css' href='{stylesheet_url}'>\n")
        
        html_file.write("</head>\n")
        html_file.write("<body>\n")
        if title:
            html_file.write(f"  <h1>{title}</h1>\n")
        paragraphs = re.split(r'\r?\n\r?\n',content)

        if content:
            for paragraph in paragraphs:
                if paragraph.strip():  # Check if the paragraph has content
                    html_file.write(f"  <p>{paragraph}</p>\n")

        html_file.write("</body>\n")
        html_file.write("</html>\n")

def process_folder(folder_path,stylesheet_url):
    if os.path.exists('til'):
        shutil.rmtree('til')
    os.makedirs('til')
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt") or file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path,stylesheet_url)

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
    parser.add_argument(
        "--stylesheet",
        "-s",
        help="URL to a CSS stylesheet to be used in the HTML files",
    )

    args = parser.parse_args()
    input_path = args.input_path
    stylesheet_url = args.stylesheet

    if os.path.isfile(input_path) and (input_path.endswith(".txt") or input_path.endswith(".md")) :
        if os.path.exists('til'):
            shutil.rmtree('til')
        os.makedirs('til')
        process_file(input_path,stylesheet_url)
    elif os.path.isdir(input_path):
        process_folder(input_path,stylesheet_url)
    else:
        print("Invalid input path. Please provide a valid file or folder path.")

if __name__ == "__main__":
    main()
