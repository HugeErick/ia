import pandas as pd
import numpy as np
from collections import Counter
import re
from sklearn.utils import resample
import os

def validateAndFixCsv(filePath):
    try:
        df = pd.read_csv(filePath)
        issues = []
        
        def handleNullValues(dataFrame):
            nullCount = dataFrame.isnull().sum()
            if nullCount.any():
                numericCols = dataFrame.select_dtypes(include=[np.number]).columns
                categoricalCols = dataFrame.select_dtypes(include=['object']).columns
                
                dataFrame[numericCols] = dataFrame[numericCols].fillna(dataFrame[numericCols].mean())
                dataFrame[categoricalCols] = dataFrame[categoricalCols].fillna(dataFrame[categoricalCols].mode().iloc[0])
                issues.append(f"Found and fixed null values in columns: {nullCount[nullCount > 0].index.tolist()}")
            return dataFrame
        
        def checkClassBalance(dataFrame):
            categoricalCols = dataFrame.select_dtypes(include=['object']).columns
            for col in categoricalCols:
                classDistribution = Counter(dataFrame[col].dropna())
                if len(classDistribution) > 1:
                    majorityClass = max(classDistribution.values())
                    minorityClass = min(classDistribution.values())
                    if majorityClass / minorityClass > 3:
                        issues.append(f"Class imbalance detected in column {col}")
                        majorityClasses = [k for k, v in classDistribution.items() if v == majorityClass]
                        minorityClasses = [k for k, v in classDistribution.items() if v == minorityClass]
                        
                        for minClass in minorityClasses:
                            minorityDf = dataFrame[dataFrame[col] == minClass]
                            upsampledMinority = resample(minorityDf, 
                                                       replace=True,
                                                       n_samples=majorityClass)
                            dataFrame = pd.concat([dataFrame[dataFrame[col] != minClass], upsampledMinority])
            return dataFrame
        
        def cleanSpecialCharacters(dataFrame):
            for col in dataFrame.columns:
                if dataFrame[col].dtype == 'object':
                    hasSpecialChars = dataFrame[col].astype(str).str.contains(r'[^a-zA-Z0-9\s]').any()
                    if hasSpecialChars:
                        dataFrame[col] = dataFrame[col].astype(str).apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))
                        issues.append(f"Cleaned special characters in column {col}")
            return dataFrame
        
        def validateLabels(dataFrame):
            invalidChars = r'[^a-zA-Z0-9_]'
            originalCols = dataFrame.columns.tolist()
            newCols = [re.sub(invalidChars, '_', col) for col in originalCols]
            
            if originalCols != newCols:
                dataFrame.columns = newCols
                issues.append("Fixed invalid characters in column names")
            
            return dataFrame
        
        df = handleNullValues(df)
        df = checkClassBalance(df)
        df = cleanSpecialCharacters(df)
        df = validateLabels(df)
        
        if not issues:
            issues.append("No issues found. Data is good to go!")
            
        dirPath = os.path.dirname(filePath)
        fileName = os.path.basename(filePath)
        baseName, ext = os.path.splitext(fileName)
        counter = 1
        outputPath = os.path.join(dirPath, f"{baseName}_cleaned{ext}")
        
        while os.path.exists(outputPath):
            outputPath = os.path.join(dirPath, f"{baseName}_cleaned_{counter}{ext}")
            counter += 1
            
        df.to_csv(outputPath, index=False)
        
        return issues, outputPath
        
    except Exception as e:
        return [f"Error processing file: {str(e)}"], None
