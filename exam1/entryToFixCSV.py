from fixCSV import validateAndFixCsv

issues, cleaned_file = validateAndFixCsv('exam1/data.csv')
for issue in issues:
    print(issue)
