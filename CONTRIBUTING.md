## Setup

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

## Using Black Formatter

### Installation

If you haven't installed Black yet, you can do so by running the following command in your terminal:

```bash
pip install black
```

### Running the Script

Make sure the script is executable:

```bash
chmod +x format_project.sh
```

Run the script to format your entire project:

```bash
./format_project.sh
```

## Using Pylint

### Installation

If you haven't installed Pylint yet, you can do so by running the following command in your terminal:

```bash
pip install pylint
```

### Running the Script

Make sure the script is executable:

```bash
chmod +x run_pylint.sh
```

Run the script to format your entire project:

```bash
./run_pylint.sh
```

## Configure Black as the Formatter:

- Open your project in VSCode.
- Ensure you have Black installed in your Python environment by running `pip install black`.
- Create a .vscode/settings.json file in your project directory if it doesn't already exist.
- Add the following content to settings.json to configure Black as the formatter:

```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
```

## Configure Pylint as the Linter:

- Open your project in VSCode.
- Ensure you have Black installed in your Python environment by running `pip install black`.
- Create a .vscode/settings.json file in your project directory if it doesn't already exist.
- Add the following content to your .vscode/settings.json file to configure Pylint as the linter:

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.pylintArgs": ["--load-plugins", "pylint_quotes"]
}
```

## Running Tests

### Requirements

1. Python
2. `unittest` module (included in Python standard library)

### Running Tests Locally

To run the tests locally, navigate to the project directory in your terminal and execute the following command:

```bash
python -m unittest test_txtToWeb.py
```

## Running Tests

### Requirements

1. Python
2. `unittest` module (included in Python standard library)

### Running Tests Locally

To run the tests locally, navigate to the project directory in your terminal and execute the following command:

```bash
python -m unittest test_txtToWeb.py
```

This command will discover and run all tests in the `test_txtToWeb.py` file.


### Contribution Guidelines

1. **Fork the Repository:** Start by forking the repository on GitHub.

2. **Create a New Branch:** Create a new branch for your contributions:

    ```bash
    git checkout -b feature/new-feature
    ```

3. **Make Changes:** Write your tests or make changes to existing tests.

4. **Run Tests Locally:** Before submitting a pull request, ensure that your tests pass locally.

    ```bash
    python -m unittest test_txtToWeb.py
    ```

5. **Commit Changes:** Commit your changes with meaningful commit messages.

    ```bash
    git commit -m "Add tests for new feature"
    ```

6. **Push Changes:** Push your changes to your forked repository.

    ```bash
    git push origin feature/new-feature
    ```

7. **Create Pull Request:** Open a pull request on the main repository to merge your changes.
