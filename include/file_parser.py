import os
import shutil
from include.markdown_converter import md_to_html
from include.html_generator import write_html_file


def extract_title_and_content(file_path):
    with open(file_path, "r") as txt_file:
        lines = txt_file.readlines()

        title = ""
        content = ""

        if file_path.endswith(".md"):
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


def process_file(input_file, stylesheet_url, lang_attribute):
    output_file = os.path.join(
        "til", os.path.splitext(os.path.basename(input_file))[0] + ".html"
    )
    title, content = extract_title_and_content(input_file)
    write_html_file(title, content, output_file, stylesheet_url, lang_attribute)


def process_folder(folder_path, stylesheet_url, lang_attribute):
    if os.path.exists("til"):
        shutil.rmtree("til")
    os.makedirs("til")
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt") or file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path, stylesheet_url, lang_attribute)
