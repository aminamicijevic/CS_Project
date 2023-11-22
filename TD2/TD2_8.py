while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        break
    except ValueError:
        print("Invalid input. Enter a number.")
