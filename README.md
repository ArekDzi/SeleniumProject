# SeleniumProject

## Introduction
This is my first test automation project based on Selenium-Webdriver with Python. It's still developing package of
automated tests of skleptest.pl demo website. The collection of tests contains:
* Register user test
* Login user tests
* Adding item do cart

## Project Structure
Here you can find a short description of main directories, and it's content

[locators](locators) - there are locators of web elements in locators.py grouped in classes\
[pages](pages) - there are sets of method for each test step\
[tests](tests) - there are sets of tests for main functionalities of website

## Getting Started
To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone
repository. You need to install packages using pip according to requirements.txt file. Run the command below in
terminal:
```
$ pip install -r requirements.txt
```

## Run Automated Tests
To run selected test without Allure report you need to set pytest as default test runner in Pycharm first
```
File > Settings > Tools > Python Integrated Tools > Testing
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow.

Tests are working on three Browsers: Chrome, Edge or Firefox\
To test on different browser in [config file](config.json) you can change name to one mentioned above. 
