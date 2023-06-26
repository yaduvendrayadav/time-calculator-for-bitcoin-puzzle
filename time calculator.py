import math

# Define the time units and their corresponding SI prefixes
time_units = {
    's': 1,
    'min': 60,
    'hr': 60 * 60,
    'day': 60 * 60 * 24,
    'week': 60 * 60 * 24 * 7,
    'month': 60 * 60 * 24 * 30,
    'year': 60 * 60 * 24 * 365
}

def calculate_time(start_range, end_range, keys_per_second):
    num_keys = int(end_range, 16) - int(start_range, 16) + 1
    time = num_keys / keys_per_second

    # Determine the appropriate time unit
    for unit in ['year', 'month', 'week', 'day', 'hr', 'min', 's']:
        if time >= time_units[unit]:
            time_value = time / time_units[unit]
            return time_value, unit

    return time, 's'

# Prompt the user to enter the range and keys per second
start_range = input("Enter the start range in hexadecimal: ")
end_range = input("Enter the end range in hexadecimal: ")
keys_per_second_input = input("Enter the keys per second (e.g., 5e, 438p): ")

# Parse the keys per second input with SI prefix
multiplier = 1
try:
    value, prefix = keys_per_second_input[:-1], keys_per_second_input[-1].lower()

    if prefix == 'k':
        multiplier = 10**3
    elif prefix == 'm':
        multiplier = 10**6
    elif prefix == 'g':
        multiplier = 10**9
    elif prefix == 't':
        multiplier = 10**12
    elif prefix == 'p':
        multiplier = 10**15
    elif prefix == 'e':
        multiplier = 10**18
    elif prefix == 'z':
        multiplier = 10**21

    keys_per_second = float(value) * multiplier

except ValueError:
    print("Invalid keys per second input. Please provide a valid input.")

else:
    # Calculate the time needed
    time_needed, time_unit = calculate_time(start_range, end_range, keys_per_second)

    # Display the result
    print(f"Time needed to cover the range: {time_needed:.2f} {time_unit}")
