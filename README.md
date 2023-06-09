# File Size Analyzer

This Python script analyzes the sizes of files in a specified directory. It provides various options to filter and display the file information.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository or download the `file.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory where the `file.py` file is located.
5. Run the script with the following command:

python file.py <directory_path> <optionchoosing>

Replace `<directory_path>` with the path to the directory you want to analyze.

6. The script will display the file information based on the chosen option.

## Options

The script provides the following options:

1. Display the 10 largest files:
python file.py <directory_path> 1

2. Display files within a specific size range (e.g., between 600 and 1000 bytes):
python file.py <directory_path> 2 

3. Display files with a specific format (e.g., ending in `.sample`):
python file.py <directory_path> 3

Feel free to explore and customize the code to suit your specific needs.

## Dependencies

This script uses the following dependencies:

- Python 3.x
- os module
- sys module

