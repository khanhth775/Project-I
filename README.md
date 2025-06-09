# Text Formatter Program
# This program was developed between August and September 2023

## Overview

This program processes a text file by reformatting its content and extracting keywords. The reformatted text ensures that no line exceeds a predefined maximum length, while meaningful keywords are identified and listed along with their line numbers.

## Features

- **Text Reformatting**: Ensures no line in the text exceeds a given maximum length.
- **Keyword Extraction**: Identifies meaningful keywords (not stop words) and records their occurrences in the text.
- **Keyword Table**: Stores the extracted keywords and their corresponding line numbers in a hash table.

## Example

### Input
A text file with long sentences.

### Output
1. A reformatted text file with no line exceeding the specified length.
2. A list of keywords and their occurrences:
Example:
ant: 3, 5, 7, 8
Aunt: 4
bold: 5, 7

## How to Use

### Prerequisites
- Python 3.x installed on your system.
- Required libraries: `pyvi`, `nltk`, `stop-words`, `tkinter`.
Install the dependencies:
```bash
pip install pyvi stop-words nltk

