#Charles Ajjan
#Week 07
#Lab 01
#Sum of Numbers
#CMP 131
#Date 10-21-2026
while user_positive_integer <= 0:
    user_input = input("Please enter a positive integer (greater than 0): ")
    
    if user_input.isdigit():
        temp_value = int(user_input)
        
        if temp_value > 0:
            user_positive_integer = temp_value
        else:
            print("Error: The number must be greater than zero. Try again.")
    else:
        print("Error: Invalid input. Please enter a valid whole number.")

accumulator = 0
for current_integer in range(1, user_positive_integer + 1):
    accumulator += current_integer

print(f"Positive integer entered: {user_positive_integer}")
print(f"Calculated sum from 1 through {user_positive_integer}: {accumulator}")
