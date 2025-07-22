while True:
    
    user_input = input("Press Enter to continue or type 'e' to exit: ")
    if user_input.lower() == 'e':
        print("Goodbye!")
        break
    try:
        n = int(input("Enter a number: "))

        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.\n")

     

