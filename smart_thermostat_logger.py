MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76

# variable for invalid value
invalid_value = 0

# initialize variable to get total temperature
total_temp = 0

# ask user for number of temperature readings
user_temperature_readings = int(input("Enter the number of temperature readings: "))

# checks if user input is valid
if user_temperature_readings <= invalid_value:
    print("Error: The number of readings must be greater than 0")
    user_temperature_readings
else:
    # loops for number of user temperature readings
    for readings in range(user_temperature_readings):
        temperature_input = int(input(f"Enter temperature reading {readings + 1}: "))
        
       # checks if temperture is valid 
        if temperature_input >= MIN_VALID_TEMP and temperature_input <= MAX_VALID_TEMP:
            total_temp = total_temp + temperature_input
            
        else:
            # traps you in a loop for invalid input 
            while temperature_input < MIN_VALID_TEMP or temperature_input > MAX_VALID_TEMP:
                print("Error: Temperature must be between 40 and 100 degrees")
                temperature_input = int(input(f"Enter temperature reading {readings + 1}: "))

# calculates average temperature
average_temp = total_temp / user_temperature_readings

# shows summary of information
print("\nSmart Thermostat Summary"
      "\n------------------------")
print(f"Average temperature: {average_temp}")
print("Readings below comfort range: ")
print("Readings above comfort range: ")