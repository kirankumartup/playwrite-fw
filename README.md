# SOM PyTest FrameWork

### Project Structure
SOM_Pytest_PW/
│
├── config/
│   ├── __init__.py
│   ├── config.yaml
│   └── ...
│
├── lib/
│   ├── __init__.py
│   ├── allure_helpers.py
│   ├── helpers.py
│   ├── webdriver_setup.py
│   └── ...
│
├── pages/
│   ├── login/
│   │   ├── __init__.py
│   │   ├── login_page.py
│   │   ├── login_page_objects.py
│   │   └── ...
│   ├── __init__.py
│   ├── base_page.py
│   └── ...
│
├── reports/
│   ├── __init__.py
│   └── ...
│
├── tests/
│   ├── login/
│   │   ├── test_login.py
│   │   └── ...
│   ├── __init__.py
│   └── ...
│
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt

## Get Started

- Clone Project from git url `git-url`
- Setup Virtual env & Configure Python Interpreter
- Run Command in Terminal `python -m venv venv`
- Activate venv `venv\Scripts\activate`
- Install python dependencies `pip install -r requirements.txt`
- Install Playwright `playwright install`

# Extentions
- Install Playwright

Download & Place Allure 
npm install -g allure-single-html

## To Run
 pytest  .\tests\test_login.py
 pytest --headed main.py

## To View Report
allure generate reports --clean 
allure generate --single-file reports --clean
allure serve reports 