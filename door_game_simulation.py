import random

def simulate_game(runs):
    # Counter 
    wins = 0

    # Run the simulation 
    for _ in range(runs):
        # Randomly select 
        winning_door = random.randint(1, 3)
        
        # Randomly select 
        contestant_choice = random.randint(1, 3)
        
        # Check the winning door
        if contestant_choice == winning_door:
            wins += 1

    # Calculate percentage
    winning_percentage = (wins / runs) * 100
    return winning_percentage

def main():
    # number of simulation runs
    number_of_runs = 100000  
    
    # Run percentage
    winning_percentage = simulate_game(number_of_runs)
    
    # Display the result
    print(f"Winning percentage after {number_of_runs} simulations: {winning_percentage:.2f}%")

# Run the main function
if __name__ == "__main__":
    main()


#Top-Down Design:
#Define the number of simulation runs (a large number for accuracy).
#For each simulation run:
   #a. Randomly choose a winning door number (1, 2, or 3).
  # b. Randomly choose a door number (1, 2, or 3) as the contestant's choice.
  # c. Check if the contestant's choice matches the winning door.
  # d. Count each win by the contestant.

# Display the winning percentage, which should be close to 33%.