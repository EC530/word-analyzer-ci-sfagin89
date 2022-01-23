# Word Analyzer - EC530 Project 1
Repo for the EC530 Project 1 Histogram Project

## Project Overview

## Required Dependencies
  The nltk and tkinter libraries are required to run the histogram script.
  Run the following CLI commands to install these libraries:
  ````
  pip install --user -U nltk
  sudo apt-get install python3-tk
  ````

## Running the Application
  There are 2 options for running the histogram script
  - Option 1: Directly from the Python interpreter
  - Option 2: Imported to a separate Python script

### Option 1: Directly from the Python Interpreter
* Step 1: From the CLI, start the python interpreter
  * ```python3```
  * Note: If python3 is already your default python version, ```python``` can be used.
* Step 2: Import the histogram python script
  * ```>>> import histogram```
* Step 3: Load a text file into the histogram object
  * ```>>> histogram.load_histogram('test.txt')```
  * Note: test.txt has been provided, but can be replaced with any text file in the same directory as histogram.py, or the full file path to another text file can be provided.
* Step 4: Print the resulting histogram
  * ```>>> histogram.print_histogram()```
* Step 5: Exit the python interpreter
  * ```exit()```

### Option 2: Imported to a separate Python script
The above steps can be performed from within a separate python script, as seen in the provided test file test_hist.py.
