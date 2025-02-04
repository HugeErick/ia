from dataBalance.dataImbalance import linearRegresion
from BFS.BFSAct3TreasureMap import BFSAct3TreasureMap
from DFS.DFSAct3Treasure import DFSAct3TreasureMap
from greedySearch.greedySearchCities import greedySearchCities
from uniformCostSearch.uniformCostSearchCities import uniformCostSearchCities
from AStarTreeSearch.AStarTreeSearchCities import AStarTreeSearchCities
from AStarGraphSearch.AStarGraphSearchCities import AStarGraphSearchCities

def displayMenu(options):
    """Display menu options and return user's choice."""
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return input()

def main():
    mainMenu = [
        "Choose exercise",
        "Exit"
    ]
    
    exerciseMenu = [
        "Data balance",
        "BFSAct3TreasureMap",
        "DFSAct3TreasureMap",
        "uniformCostSearchCities"
        "greedySearchCities"
        "AStarTreeSearchCities"
        "AStarGraphSearchCities"
        "Back",
        "Exit"
    ]
    
    # manual ass mapping
    exerciseActions = {
        "1": linearRegresion,
        "2": BFSAct3TreasureMap,
        "3": DFSAct3TreasureMap,
        "4": uniformCostSearchCities,
        "5": greedySearchCities,
        "6": AStarTreeSearchCities,
        "7": AStarGraphSearchCities,
        "8": lambda: None,  # Back action
        "9": exit
    }
    
    while True:
        print("\nhello pls choose")
        choice = displayMenu(mainMenu)
        
        if choice == "1":
            while True:
                print()
                print("Exercises:")
                exerciseChoice = displayMenu(exerciseMenu)
                
                if exerciseChoice in exerciseActions:
                    action = exerciseActions[exerciseChoice]
                    if exerciseChoice == "8":  # Back option
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
