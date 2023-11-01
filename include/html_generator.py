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

        # Add the search bar HTML form
        html_file.write("<div style='margin-bottom: 20px;'>")
        html_file.write("<form id='search-form'>")
        html_file.write("  <input type='text' id='search-input' placeholder='Search...'>")
        html_file.write("  <input type='submit' value='Search'>")
        html_file.write("</form>")
        html_file.write("</div>")


        if title:
            html_file.write(f"  <h1>{title}</h1>\n")
            
        paragraphs = re.split(r'\r?\n\r?\n', content)

        html_file.write("<div id='content'>")
        if content:
            for paragraph in paragraphs:
                if paragraph.strip():  # Check if the paragraph has content
                    html_file.write(f"  <p>{paragraph}</p>\n")
        html_file.write("</div>")

                # Add JavaScript code to handle search and highlight functionality
        html_file.write("<script>")
        html_file.write("document.getElementById('search-form').addEventListener('submit', function(event) {")
        html_file.write("  event.preventDefault();")
        html_file.write("  var searchTerm = document.getElementById('search-input').value;")
        html_file.write("  var content = document.getElementById('content');")
        html_file.write("  var regex = new RegExp(searchTerm, 'gi');")
        html_file.write("  content.innerHTML = content.innerHTML.replace(regex, function(match) {")
        html_file.write("    return '<span style=\"background-color: yellow;\">' + match + '</span>';")
        html_file.write("  });")
        html_file.write("});")
        html_file.write("</script>")

        html_file.write("</body>\n")
        html_file.write("</html>\n")