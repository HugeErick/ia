def logisticGrowth(initialPop, growthRate, carryingCapacity, years):
    """
    Calculate population growth using the logistic model.
    
    Parameters:
    initialPop (float): Starting population size (P₀)
    growthRate (float): Growth rate (r) between 0 and 1
    carryingCapacity (float): Maximum sustainable population (K)
    years (int): Number of years to model
    
    Returns:
    list: Population sizes for each year
    """
    # Initialize with starting population
    results = [initialPop]
    
    def nextYear(t):
        if t >= years:
            return
        
        prevPop = results[t]
        curPop = prevPop + growthRate * prevPop * (1 - prevPop / carryingCapacity)
        results.append(curPop)
        
        nextYear(t + 1)
    
    # Start recursion
    nextYear(0)
    return results

# Example
def runLogisticGrowth():
    pop = logisticGrowth(100, 0.1, 1000, 10)
    for year, value in enumerate(pop):
        print(f"Year {year}: {value:.2f}")

# Run in Google Collab:
#runlogisticGrowth()
