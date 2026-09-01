print("="*5,"Temperature Conversion","="*5)
choice = 0
while choice != 3:
    print("1. Celcious to ferenheit.")
    print("2. ferenheit to celcious.")
    print("Exit.")
    choice = int(input("Enter a choice between 1-3: "))
    if choice == 1:
        celcious = int(input("Enter temp in celcious: "))
        ferenheit = (celcious *9/5)+32
        print("\nTemperature in Ferenheit is ",ferenheit)
    elif choice == 2:
        ferenheit = int(input("Enter temp in ferenheit: "))
        celcios = (ferenheit - 32)*(5/9)
        print("\nTemperature in celcios is ",celcious)
    elif choice ==3:
        print("Good bye!")
        print()
else:
        print("Invalid input.")
    
        
