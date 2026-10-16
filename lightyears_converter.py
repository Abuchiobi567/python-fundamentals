# conversion 
CONVERSION_FACTOR = 0.00000000000010570

# loop
while True:
    try:
        # user  input 
        lightyears = float(input("Enter the value in lightyears (LY): "))

        # Calculate  distance 
        kilometres = lightyears / CONVERSION_FACTOR

        # Display  result
        print(f"{lightyears} lightyears is approximately {kilometres:.2e} kilometres.")

    except ValueError:
        print("Please enter a valid  value for lightyears.")

    #  if the user wants to perform another conversion
    repeat = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Goodbye!")
        break