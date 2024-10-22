
#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.
#solution

# Initial list of favorite foods
favorite_foods = ["RICE", "MATOOKE", "IRISH", "CASSAVA", "SWEETPOTATO"]

# Adding two more items to the list
favorite_foods.append("YAMS")
favorite_foods.append("BLACK YAM")

# Removing one item from the list
favorite_foods.remove("CASSAVA")

# Printing the updated list
print("Updated list of favorite foods:")
print(favorite_foods)



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.
#solution
# Given list of numbers
numbers = [2, 5, 8, 10, 3, 6]

# Print the first and last elements of the list
first_element = numbers[0]
last_element = numbers[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")

# Print the list in reverse order
reversed_numbers = numbers[::-1]
print("List in reverse order:", reversed_numbers)

# Calculate and print the sum of all the elements in the list
total_sum = sum(numbers)
print("Sum of all elements:", total_sum)
