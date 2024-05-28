################################
# Github Repo link
# Yeshi Wangmo
# BBI "B"
# 03230424
################################
# REFERENCES
# https://youtube.com/playlist?list=PLVJiPhsW8Gnf5rQCOXoptugEtJneB0ZOd&si=IaAtCAKC8Io3RqgB
# https://youtu.be/4NvLznuITH0?si=nf_R9cvzkRvMHWBs
#https://youtu.be/qjrRf_pXWFQ?si=B4Xbm6Kk3FnHCF5q
################################
# SOLUTION
# Your Solution Score: <total sum>
################################


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

# Solution
def print_solution(lines):
    total_sum = 0
    for line in lines:
        # Extract the first and last characters of each line
        first_digit = int(line[0])
        last_digit = int(line[-1])
        # Form the two-digit number and add it to the total sum
        total_sum += int(str(first_digit) + str(last_digit))
    return total_sum

# Main part of the code
if __name__ == "__main__":
    # Replace 'input.txt' with the actual name of your input file
    file_name = '424.txt'
    lines = read_input(file_name)
    
    # Calculate and print the solution
    total_sum = print_solution(lines)
    print(f"The total sum from the given input file {file_name} is {total_sum}")
