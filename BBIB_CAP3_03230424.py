################################
# Github Repo link
# Yeshi Wangmo
# BBI "B"
# 03230424
################################
# REFERENCES
# https://youtube.com/playlist?list=PLVJiPhsW8Gnf5rQCOXoptugEtJneB0ZOd&si=IaAtCAKC8Io3RqgB
# https://youtu.be/4NvLznuITH0?si=nf_R9cvzkRvMHWBs
# https://youtu.be/qjrRf_pXWFQ?si=B4Xbm6Kk3FnHCF5q
################################
# SOLUTION
# Solution Score: 484171.
################################
def read_input(file_path):
    #initialize the sum as 0
    total_sum = 0
    
    # open .txt file and read it line by line
    with open(file_path, 'r') as file:
        line_number = 1
        for line in file:
            #removing charatertsand whitespace
            cleaned_line = line.strip()
            
            # variable to store the first and last digit 
            first_digit = None
            last_digit = None
            
            # loop through characterr to find first digit
            for char in cleaned_line:
                if char.isdigit():
                    first_digit = char
                    break
            
            # Loop through the characters  to find the last digit
            for char in reversed(cleaned_line):
                if char.isdigit():
                    last_digit = char
                    break
            
            # Check if both digits were found
            if first_digit is not None and last_digit is not None:
                # Combine them into a two-digit number
                two_digit_number = int(first_digit + last_digit)
                
                # Printing the line number and two digit
                print(f"Line {line_number}'s number is: {two_digit_number}")
                
                # adding two digit to the sm
                total_sum += two_digit_number
            
            # Increment the line number
            line_number += 1
    
    return total_sum

def print_solution(file_path):
    total_sum = read_input(file_path)
    print(f"The total sum from the given input file {file_path} is {total_sum}")


file_path = '424.txt'  
print_solution(file_path)
