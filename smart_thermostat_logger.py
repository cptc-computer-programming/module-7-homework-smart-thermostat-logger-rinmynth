MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76

# variable for invalid value
invalid_value = 0

# initialize variable to get total temperature
total_temp = 0

# initialize variable to count readings above comfort range
above_comfort_count = 0

# initialize variable to count readings below comfort range
below_comfort_count = 0

# ask user for number of temperature readings
user_temperature_readings = int(input("Enter the number of temperature readings: "))

# checks if user input is valid
while user_temperature_readings <= invalid_value:
    print("Error: The number of readings must be greater than 0")
    user_temperature_readings = int(input("Enter the number of temperature readings: "))

# loops for number of user temperature readings
for readings in range(user_temperature_readings):
    temperature_input = int(input(f"Enter temperature reading {readings + 1}: "))

    # traps you in a loop for invalid input for temperature
    while temperature_input < MIN_VALID_TEMP or temperature_input > MAX_VALID_TEMP:
        print("Error: Temperature must be between 40 and 100 degrees")
        temperature_input = int(input(f"Enter temperature reading {readings + 1}: "))
        
    # checks if temperture is valid 
    if temperature_input >= MIN_VALID_TEMP and temperature_input <= MAX_VALID_TEMP:
        total_temp = total_temp + temperature_input
            
        valid_temp_readings = user_temperature_readings

        # gets count below comfort range
        if temperature_input < COLD_LIMIT:
            below_comfort_count += 1
        # gets count above comfort range
        elif temperature_input > WARM_LIMIT:
            above_comfort_count += 1

# calculates average temperature
average_temp = total_temp / valid_temp_readings

# shows summary of information
print("\nSmart Thermostat Summary"
      "\n------------------------")
print(f"Average temperature: {average_temp: .1f}")
print("Readings below comfort range: ", below_comfort_count)
print("Readings above comfort range: ", above_comfort_count)