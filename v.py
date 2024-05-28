# def read_input(file_path):
#     # Initialize the sum variable
#     total_sum = 0
    
#     # Open the file and read it line by line
#     with open(file_path, 'r') as file:
#         for line in file:
#             # Remove newline characters and strip whitespace
#             cleaned_line = line.strip()
            
#             # Check if the line has at least one character
#             if cleaned_line:
#                 # Extract the first and last characters
#                 first_char = cleaned_line[0]
#                 last_char = cleaned_line[-1]
                
#                 # Check if both characters are digits
#                 if first_char.isdigit() and last_char.isdigit():
#                     # Combine them into a two-digit number and add it to the sum
#                     total_sum += int(first_char + last_char)
    
#     return total_sum

# # Example usage
# file_path = '424.txt'  # Replace 'your_file.txt' with the path to your text file
# total_sum = read_input(file_path)
# print(f'The total sum of the first and last digit of each line is {total_sum}.')




# Read the input.txt file
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

# Extract first and last digit from the line and form a two-digit number
def extract_numbers_from_line(line):
    first_digit = None
    last_digit = None
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    return None

# Solution to calculate the total sum
def calculate_total_sum(lines):
    total_sum = 0
    for i, line in enumerate(lines, 1):
        number = extract_numbers_from_line(line.strip())
        if number is not None:
            print(f"Line {i}’s number is: {number}")
            total_sum += number
    return total_sum

# Print the solution
def print_solution(file_name):
    lines = read_input(file_name)
    total_sum = calculate_total_sum(lines)
    print(f"The total sum from the given input file {file_name} is {total_sum}")

# Example usage
file_name = '424.txt'
print_solution(file_name)
