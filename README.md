# playwright-python

## Description

This is a Python project, dedicated to enhancing my learnings for both Python and Playwright. Playwright is seen as the successor to Selenium. It is deemed to be faster, more reliable and easier to work with and for this project I am going to explore Playwright in combination with Python.

## Requirements

### Installing Dependencies and Dummy Run
This Python project assumes your using a virtual environment. After cloning this project, from the root directory you will need to:

1. Set up a local virtual environment
```
python3 -m venv venv
```
2. Activate it
```
source venv/bin/activate
```
4. Install the required dependencies
```
pip install -r requirements.txt
```
5. Run the example script to make sure it's working
```
python project-test/main.py
```
6. Deactivate the virtual environment
```
deactivate
```
If you were able to run the main.py inside the project-test folder and you can see a screenshot then this should be enough to run the remaining other python files in this project.

## Learning Notes

Playright provides both sync and async (see sample-tests). 

Sync tests use blocking based code and each line of code that run waits for the previous line to finish before it run. 

Async lines of code do not wait and need to have await's on them to achieve the same behaviour.

Sync based tests are good for sequential based tests i.e. one user going through a web session (user log in).

Async based tests are good for tests where you need multiple actions happening.

