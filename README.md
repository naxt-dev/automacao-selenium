# Web Test Automation — Python & Selenium

Web test automation project using Python, Selenium WebDriver and unittest, covering login, form validation and error handling.

## Technologies

- Python
- Selenium WebDriver
- unittest
- Git
- GitHub

## Project Objective

The objective of this project is to practice and demonstrate foundational knowledge in web test automation, application behavior validation, and software quality practices.

It focuses on using Python and Selenium WebDriver to interact with web pages, validate form inputs, and verify that web interfaces handle valid and invalid inputs correctly.

## Test Scenarios

- Automated navigation to web pages
- Form field interaction and data submission
- Login interface testing
- Validation of valid credentials and expected successful responses
- Validation of invalid credentials and handling of invalid inputs
- Verification of error messages and error states
- Identification of incorrect application responses against expected behaviors

## Project Structure

```text
automacao-selenium/
├── pages/
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   └── test_login.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x
- Supported web browser (e.g., Google Chrome or Microsoft Edge)
- Corresponding WebDriver

### Clone the repository

```bash
git clone https://github.com/naxt-dev/automacao-selenium.git
cd automacao-selenium
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\venv\Scripts\activate
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install selenium
```

### Run the tests

Run the test suite using unittest test discovery:

```bash
python -m unittest discover -s tests -v
```

## What I Learned

- Web test automation with Selenium WebDriver
- Automated interaction with web elements
- Test organization using unittest
- Validation of expected application behaviors
- Identification of incorrect application responses
- Basic software quality and testing practices
- Structuring automated test scenarios

## Future Improvements

- Expanding test coverage across more application features
- Adding more negative and edge-case scenarios
- Improving test organization and code reusability
- Adding test execution reports
- Integrating automated tests into CI/CD pipelines
- Exploring other testing frameworks and automation tools
