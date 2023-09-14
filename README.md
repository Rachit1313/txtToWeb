# txtToWeb

`txtToWeb` is a command-line tool for converting text files to HTML content. It allows you to easily generate HTML files from plain text documents with optional features like specifying a CSS stylesheet.

## Features

- Convert text files to valid HTML5 documents.
- Automatically detect titles and format content into paragraphs.
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

To convert all .txt files in a directory:
```bash
txtToWeb.py /path/to/directory
```

To convert all .txt files in a directory and include a CSS stylesheet:
```bash
./txtToWeb.py -s https://example.com/style.css /path/to/directory
```

### Flags

* `--version` or `-v`: Display the tool's version.
* `--stylesheet` or `-s`: Specify a URL to a CSS stylesheet to include in the HTML files.
* `--help` or `-h`: Display usage information and available flags.

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
