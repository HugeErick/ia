from dataBalance.dataImbalance import linearRegresion
from BFS.BFSAct3TreasureMap import BFSAct3TreasureMap
from DFS.DFSAct3Treasure import DFSAct3TreasureMap
from greedySearch.greedySearchCities import greedySearchCities
from optimization.optimizationMethods import runMethods
from uniformCostSearch.uniformCostSearchCities import uniformCostSearchCities
from AStarTreeSearch.AStarTreeSearchCities import AStarTreeSearchCities
from AStarGraphSearch.AStarGraphSearchCities import AStarGraphSearchCities
from optimization.optimizationMethods import runMethods
from nonMonotonic.nonMonotonicSystem import runNonMonotonics
from recursiveLogistic.LogisticRecursive import runLogisticGrowth

def displayMenu(options):
    """Display menu options and return user's choice."""
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return input()

def main():
    mainMenu = [
        "1: Choose exercises partial 1",
        "2: Choose exercises partial 2",
        "3: Exit"
    ]
    
    exerciseMenuPartial1 = [
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

    exerciseMenuPartial2 = [
        "Optimization methods",
        "Non monotonics methods",
        "run recursive system",
        "Back",
        "Exit",
    ]

    
    # manual ass mapping
    exerciseActionsPartial1 = {
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
    
    exerciseActionsPartial2 = {
        "1": runMethods,
        "2": runNonMonotonics,
        "3": runLogisticGrowth,
        "4": lambda: None,  # Back action
        "5": exit
    }

    while True:
        print("\nhello pls choose")
        choice = displayMenu(mainMenu)
        
        if choice == "1":
            while True:
                print()
                print("Exercises:")
                exerciseChoice = displayMenu(exerciseMenuPartial1)
                
                if exerciseChoice in exerciseActionsPartial1:
                    action = exerciseActionsPartial1[exerciseChoice]
                    if exerciseChoice == "8":  # Back option
                        break
                    action()
                else:
                    print("Invalid option, please try again")
        
        elif choice == "2":
            while True:
                print()
                print("Exercises:")
                exerciseChoice = displayMenu(exerciseMenuPartial2)
                
                if exerciseChoice in exerciseActionsPartial2:
                    action = exerciseActionsPartial2[exerciseChoice]
                    if exerciseChoice == "4":  # Back option
                        break
                    action()
                else:
                    print("Invalid option, please try again")

        elif choice == "3":
            break
        else:
            print("Invalid option, please try again")

if __name__ == "__main__":
    main()
