try:
    while True:
        try:
            user_input = input("Enter a number: ")
            number = int(user_input)
            break
        except ValueError:
            print("Invalid input. Enter a number.")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt: Program terminated by the user.")
