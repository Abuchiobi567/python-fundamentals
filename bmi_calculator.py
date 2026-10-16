def main():
    # User input  
    name = input("Enter your name: ")
    weight_kg = float(input("Enter your weight in kilograms (kg): "))
    height_cm = float(input("Enter your height in centimetres (cm): "))

    # Convert height from cm to metres for the BMI calculation
    height_m = height_cm / 100

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "underweight"
    elif 18.5 <= bmi < 25.0:
        category = "healthy"
    elif 25.0 <= bmi < 30.0:
        category = "overweight"
    else:
        category = "obese"

    # Format output to two decimal places for BMI
    output_line = f"{name}, {height_cm} cm, {weight_kg} kg, BMI: {bmi:.2f}, Category: {category}"

    # Display the output
    print(output_line)

# Run the main function
if __name__ == "__main__":
    main()