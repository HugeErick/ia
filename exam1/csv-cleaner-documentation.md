# CSV Validation and Cleaning Script Documentation

## Overview
This implementation provides a robust CSV file validation and cleaning system consisting of two scripts: `entryToFixCSV.py` and `fixCSV.py`. The system performs various data cleaning operations including handling null values, addressing class imbalance, removing special characters, and validating column labels.

## Scripts Structure

### entryToFixCSV.py
Entry point script that demonstrates usage of the CSV validation system.
```python
from fixCSV import validateAndFixCsv

issues, cleaned_file = validateAndFixCsv('exam1/data.csv')
for issue in issues:
    print(issue)
```

### fixCSV.py
Main implementation containing the validation and cleaning logic.

## Main Function
```python
def validateAndFixCsv(filePath)
```
### Parameters
- `filePath`: String path to the input CSV file

### Returns
- Tuple containing:
  1. List of issues found and fixed
  2. Path to the cleaned output file

## Core Cleaning Functions

### handleNullValues
```python
def handleNullValues(dataFrame)
```
- Identifies and handles null values in the dataset
- Numeric columns: Fills nulls with mean values
- Categorical columns: Fills nulls with mode values
- Reports columns where null values were found

### checkClassBalance
```python
def checkClassBalance(dataFrame)
```
- Detects class imbalance in categorical columns
- Identifies when majority/minority class ratio exceeds 3:1
- Performs upsampling on minority classes using sklearn's resample
- Reports columns with class imbalance issues

### cleanSpecialCharacters
```python
def cleanSpecialCharacters(dataFrame)
```
- Removes special characters from object/string columns
- Keeps only alphanumeric characters and spaces
- Reports columns where special characters were cleaned

### validateLabels
```python
def validateLabels(dataFrame)
```
- Validates column names
- Replaces invalid characters with underscores
- Reports if column names were modified

## File Handling
- Creates cleaned output file with "_cleaned" suffix
- Handles naming conflicts by adding incremental counters
- Preserves original file directory structure

## Dependencies
- pandas: Data manipulation and CSV handling
- numpy: Numerical operations
- sklearn.utils: For resampling functionality
- collections: For Counter class
- re: Regular expression operations
- os: File path handling

## Example Usage
```python
from fixCSV import validateAndFixCsv

# Process a CSV file
issues, cleaned_file_path = validateAndFixCsv('path/to/your/file.csv')

# Print any issues found
for issue in issues:
    print(issue)

# cleaned_file_path contains the path to the cleaned CSV
```

## Error Handling
- Wraps all operations in try-except block
- Returns error message if file processing fails
- Returns None as cleaned_file path in case of errors

## Notes
- Creates backup by saving to new file instead of overwriting
- Handles both numerical and categorical data appropriately
- Provides detailed feedback about all modifications made
- Maintains data integrity while cleaning
