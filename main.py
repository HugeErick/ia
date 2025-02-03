from dataBalance.dataImbalance import linearRegresion
from BFS.BFSAct3TreasureMap import BFSAct3TreasureMap

def displayMenu(options):
    """Display menu options and return user's choice."""
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return input()

def main():
    # Define menu options as lists
    mainMenu = [
        "Choose exercise",
        "Exit"
    ]
    
    exerciseMenu = [
        "Data balance",
        "BFSAct3TreasureMap",
        "Back",
        "Exit"
    ]
    
    # Menu action mappings
    exerciseActions = {
        "1": linearRegresion,
        "2": BFSAct3TreasureMap,
        "3": lambda: None,  # Back action
        "4": exit
    }
    
    while True:
        print("\nhello pls choose")
        choice = displayMenu(mainMenu)
        
        if choice == "1":
            while True:
                print()  # Empty line for spacing
                exerciseChoice = displayMenu(exerciseMenu)
                
                if exerciseChoice in exerciseActions:
                    action = exerciseActions[exerciseChoice]
                    if exerciseChoice == "3":  # Back option
                        break
                    action()
                else:
                    print("Invalid option, please try again")
        
        elif choice == "2":
            break
        else:
            print("Invalid option, please try again")

if __name__ == "__main__":
    main()
