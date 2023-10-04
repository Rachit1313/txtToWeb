# txtToWeb

`txtToWeb` is a command-line tool for converting text files to HTML content. It allows you to easily generate HTML files from plain text documents with optional features like specifying a CSS stylesheet.

## Features

- Convert text and Markdown files to valid HTML5 documents.
- Automatically detect titles and format content into paragraphs.
- Parse Markdown syntax for Italics and convert it to HTML.
- Optionally include a CSS stylesheet in the HTML output.
- Process individual files or entire directories of text files.

## Usage

### Requirements

1. bash/zsh/wsl Terminal
2. Python

### Installation

1. Clone this repository to your local machine:

```bash
   git clone https://github.com/your-username/txtToWeb.git
```

2. Navigate to the txtToWeb directory:

```bash
   cd txtToWeb
```

3. Make it executable

```bash
    chmod +x txtToWeb.py
```

### Basic Usage

To convert a single text file to HTML:

```bash
./txtToWeb.py <filename>
```

To add a stylesheet to the file:

```bash
./txtToWeb.py -s https://example.com/style.css <filename>
```

To convert all .txt and .md files in a directory:

```bash
txtToWeb.py /path/to/directory
```

To convert all .txt and .md files in a directory and include a CSS stylesheet:

```bash
./txtToWeb.py -s https://example.com/style.css /path/to/directory
```

To use TOML config:

```bash
txtToWeb.py -c /path/to/config /path/to/directory or file
```

### Flags

- `--version` or `-v`: Display the tool's version.
- `--stylesheet` or `-s`: Specify a URL to a CSS stylesheet to include in the HTML files.
- `--help` or `-h`: Display usage information and available flags.
- `--config` or `-c`: URL to a TOML config file to be used as a config for the HTML files.

## Markdown Support

As of the latest update, `txtToWeb` has incorporated support for converting Markdown `.md` files in addition to plain text files. This introduces the capability to parse specific Markdown syntax and convert it to valid HTML5 format, allowing for enhanced content structuring and formatting.

### Italic Syntax

The initial release of Markdown support focuses on the Italic syntax. Users can now write text in Italics in their Markdown files, and `txtToWeb` will correctly convert it into HTML. The Italic text can be written by wrapping the desired text segment with either single asterisks `*` or single underscores `_`.

### Config Example

stylesheet = "../examples/txtToWeb/styles.css"

lang = "en-US"

#### Usage Example:

Markdown Input:

```markdown
This is an _italic_ example.
And this is another _italic_ example.
```

Generated HTML Output:

```html
<p>This is an <i>italic</i> example.</p>
<p>And this is another <i>italic</i> example.</p>
```

### Output

By default, the tool generates HTML files in a txtToWeb directory in the current working directory. Each HTML file corresponds to a processed text file, with the original filename.

### Example

Command:

```bash
./txtToWeb.py -s https://cdnjs.cloudflare.com/ajax/libs/tufte-css/1.8.0/tufte.min.css test.txt
```

Sample Input: [test.txt](examples/test.txt)

Output: [test.html](examples/txtToWeb/test.html)

Output Hosted: [https://txttoweb.netlify.app/](https://txttoweb.netlify.app/)

### License

This project is licensed under the GNU General Public License v3.0 License - see the [LICENSE](LICENSE) file for details.
