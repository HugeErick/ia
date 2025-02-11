import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# List of CSV file names
csvFiles = ["iris.csv", "Iris1.csv", "Iris2.csv", "Iris3.csv"]

for fileName in csvFiles:
    try:
        # Load the dataset, skipping bad lines
        dataFrame = pd.read_csv(f"/home/erick/ia/dataBalance/{fileName}", on_bad_lines="skip")

        # Drop non-numeric columns
        dataFrameNumeric = dataFrame.select_dtypes(include=["number"])

        # Compute the correlation matrix
        correlationMatrix = dataFrameNumeric.corr()

        # Print the correlation matrix
        print(f"Correlation Matrix for {fileName}:\n")
        print(correlationMatrix, "\n")

        # Plot the heatmap and save it
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlationMatrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title(f"Correlation Matrix - {fileName}")

        # Save the plot instead of using plt.show()
        plt.savefig(f"correlationMatrix_{fileName}.png")
        plt.close()

    except Exception as exception:
        print(f"Error processing {fileName}: {exception}")

