# Data Balance Project

This project demonstrates data balancing techniques for machine learning, including oversampling and undersampling methods.

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
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```
python main.py
```

### Menu Navigation

The program presents a menu-driven interface:

1. Main Menu:
   - Choose "1" to select an exercise
   - Choose "2" to exit the program

2. Exercise Menu:
   - Choose "1" for Data balance exercise
   - Choose "2" to go back to the main menu
   - Choose "3" to exit the program

3. When you select the Data balance exercise, it will run the `linearRegresion1()` function, which performs the following:
   - Loads and preprocesses the data
   - Displays class distribution and plots for the original imbalanced data
   - Applies oversampling (SMOTE), undersampling, and a combination of both
   - Trains logistic regression models on each dataset
   - Displays classification reports and plots for each scenario

## Extra 

### Questions from activity of data balance
1. How did the model's performance change after balancing the data?
   Ans: The model did in fact improve the ability to not make mistakes. If not obvious, this greatly increases the chance of a correct prediction for the classification prediction and, as said before, the precision.

2. Which technique (oversampling or undersampling) was more effective, and why?
   Ans: Oversampling conquers over undersampling due to the data balance that oversampling normally achieves. This isn't always the case, but in a normal scenario, we would want to balance the data as much as possible.

3. Which metrics are most useful for evaluating models in problems with imbalanced classes?
   Ans: In my humble opinion, I would say precision, recall, and accuracy. All of them calculate a strict precision based on what data can be wrong or truthful.

## Contact Information

For any questions or feedback, please contact:

Erick Gonzalez Parada
Email: erick.parada101@gmail.com
GitHub: https://github.com/HugeErick/ia.git
