from interest_formulas import Interest_Calculator as IC

greeting = "Interest Calculator Version 1"
instructions = "\n\nPlease note: \n\tDo not enter interest rates as decimals, i.e., input 10% as 10 and not .10 \n\tEnter time in years and not months or days.\n"
print(greeting + instructions)



while True:
    option = input("Which calculation would you like to perform (type the two letter code): \n\tSI for Simple Interest \n\tCI for Compunt Interest  \n\tCCI for Continuous Compount Interest\n").upper()
    if  option == 'SI':
        formula = IC.simple_interest()
    elif option == 'CI':
        formula = IC.compound_interest()
    elif option == 'CCI':
        formula = IC.continuous_compound_interest()
    else:
        continue
    repeat = input("\nNew Calculation (y/n)?\n")
    if repeat == 'y':
        continue
    else:
        break
