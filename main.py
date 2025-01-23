from dataBalance.dataImbalance import linearRegresion1

def main():
    rawInputAns=True
    exerciseRawInputAns=True
    print("hello pls choose")
    while rawInputAns:
        print("""
            1. Choose exercise
            2. Exit 
              """)
        rawInputAns= input()
        if rawInputAns == "1":
            while exerciseRawInputAns:
                print("""
                        1. Data balance
                        2. Back
                        3. Exit
                      """)
                exerciseRawInputAns = input()
                if exerciseRawInputAns == "1":
                    linearRegresion1()
                elif exerciseRawInputAns == "2":
                    break
                else:
                    exit()
        else:
            break

if __name__ == "__main__":
    main()
