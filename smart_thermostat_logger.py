MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76

# variable for invalid value
invalid_value = 0

# ask user for number of temperature readings
user_temperature_readings = int(input("Enter the number of temperature readings: "))

# checks if user input is valid
if user_temperature_readings <= invalid_value:
    print("Error: The number of readings must be greater than 0")
    user_temperature_readings
else:
    print("good")