# Data Balance Project

This project demonstrates data balancing techniques for machine learning, including oversampling and undersampling methods, along with various search algorithms and optimization techniques.

[!WARNING]
This method was unsustainable, for code retreival there will be a collab link or a pdf with the collab link all the times.

## Setup

### Requirements
- Python 3.x
- Git (optional, for cloning the repository)

### Installation

1. Clone the repository (optional):
   ```
   git clone https://github.com/HugeErick/ia.git
   ```
   Alternatively, you can download the raw Python files directly.

2. Navigate to the project directory:
   ```
   cd ia
   ```

3. (Optional) Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r {package}
   ```

## Usage

Run the main script:

```
python main.py
```

### Menu Navigation

The program presents a menu-driven interface with two main sections:

1. **Main Menu:**
   - Choose "1" to select an exercise from Partial 1
   - Choose "2" to select an exercise from Partial 2
   - Choose "3" to exit the program

2. **Exercise Menu Partial 1:**
   - Choose "1" for Data Balance
   - Choose "2" for BFS Treasure Map
   - Choose "3" for DFS Treasure Map
   - Choose "4" for Uniform Cost Search Cities
   - Choose "5" for Greedy Search Cities
   - Choose "6" for A* Tree Search Cities
   - Choose "7" for A* Graph Search Cities
   - Choose "8" to go back to the main menu
   - Choose "9" to exit

3. **Exercise Menu Partial 2:**
   - Choose "1" for Optimization Methods
   - Choose "2" to go back to the main menu
   - Choose "3" to exit

### Data Balance Exercise
When you select the **Data Balance** exercise, it will execute the `linearRegresion()` function, which performs the following:
   - Loads and preprocesses the data
   - Displays class distribution and plots for the original imbalanced data
   - Applies oversampling (SMOTE), undersampling, and a combination of both
   - Trains logistic regression models on each dataset
   - Displays classification reports and plots for each scenario

## Compatibility
All scripts have been tested and run without issues in **Google Colab**, making it an easy-to-use environment for execution and experimentation.

## Extra

### Questions from the Data Balance Exercise
1. **How did the model's performance change after balancing the data?**
   - The model improved its ability to make fewer mistakes, increasing the accuracy of classification predictions and precision.

2. **Which technique (oversampling or undersampling) was more effective, and why?**
   - Oversampling generally performs better because it balances the data effectively, though this is not always the case in every scenario.

3. **Which metrics are most useful for evaluating models in problems with imbalanced classes?**
   - Precision, recall, and accuracy are crucial for determining the correctness and effectiveness of the model.

## Contact Information

For any questions or feedback, please contact:

**Erick Gonzalez Parada**  
Email: erick.parada101@gmail.com  
GitHub: [https://github.com/HugeErick/ia](https://github.com/HugeErick/ia)


