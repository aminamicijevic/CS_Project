import random


# Defining a function which will be called 1000 times to get the winning percentage
# It simulates one round of the game
def game_simulator():
    # Randomly choosing the doors which will have the car behind them
    doors_with_a_car_behind_them = random.randint(1, 3)

    # Contestants initial choice
    contestants_choice = random.randint(1, 3)

    # Determining which doors have goats behind them, excluding the contestants initial choice
    doors_with_goats_behind_them = [i for i in [1, 2, 3] if i != contestants_choice
                                    and i != doors_with_a_car_behind_them]

    # The host choosing the doors with a goat behind them to open
    hosts_choice = random.choice(doors_with_goats_behind_them)

    # Contestant switching his choice to remaining doors
    remaining_doors = [i for i in [1, 2, 3] if i != contestants_choice
                       and i != hosts_choice]
    new_contestants_choice = remaining_doors[0]

    # Checking if the contestant won by switching doors
    did_he_win = new_contestants_choice == doors_with_a_car_behind_them

    return did_he_win


# Function that will run the simulation multiple times to determine the winning percentage
def main():
    number_of_simulations = 1000
    number_of_wins = sum(game_simulator() for _ in range(number_of_simulations))

    # Calculating the winning percentage
    winning_percentage = (number_of_wins / number_of_simulations) * 100

    # Printing out the winning percentage
    print(f"The winning percentage is {winning_percentage:.2f}%")


# Calling the function to start the simulation
main()
