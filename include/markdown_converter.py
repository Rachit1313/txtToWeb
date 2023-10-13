import re

def md_to_html(content):
    # Convert Markdown italic syntax to HTML
    content = re.sub(r"([*_])([^*_]*)(\1)", r"<i>\2</i>", content)
    # Convert Markdown horizontal rule syntax to HTML <hr> tag
    content = re.sub(r"(?m)^---\s*$", r"<hr>", content)
    return content
