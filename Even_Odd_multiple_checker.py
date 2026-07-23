print("=========== Even / Odd / Multiple of 5? ===========")
Num = int(input("Enter a number : "))
if Num % 2 == 0:
    print("\n It is an even number.")
    if Num % 5 == 0: 
        print("It is also Multiple of 5.")
    else: 
        print("It is not multiple of 5.")
else:
    print("\nIt is an Odd number.")
    if Num % 5 == 0:
        print("It is multiple of 5.")
    else: 
        print("It is not multiple of 5.")

