import os
import re

def write_html_file(title, content, output_file, stylesheet_url, lang_attribute):
    with open(output_file, "w") as html_file:
        html_file.write("<!doctype html>\n")
        html_file.write(f"<html lang='{lang_attribute}'>\n")
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
        paragraphs = re.split(r'\r?\n\r?\n', content)

        if content:
            for paragraph in paragraphs:
                if paragraph.strip():  # Check if the paragraph has content
                    html_file.write(f"  <p>{paragraph}</p>\n")

        html_file.write("</body>\n")
        html_file.write("</html>\n")