"""
Day 3 – More Variables & Arithmetic

Goal: practice reassigning variables, string expressions, and numeric operators (+, -, *, /). Understand difference between string and number addition.
"""

# Updating variables
status = "Playing football"
print(status)
status = "Walking the dog"
print(status)

# Expression with strings
followers = "55"
print("Followers:" + followers)
label = "Posts:" + "13"
print(label)

# Store expression as variable and display
posts_label = "Posts:" + "13"
print(posts_label)

# Using variables in expressions
temperature = "14"
print(temperature + " degrees")

title = "Ms. "
name = "Irene"
print(title + name)

# Numeric expressions
active_users = 5
print(active_users)

number_of_applications = 5 + 1
print(number_of_applications)

percent = 0.5 * 100
print(percent)

number_of_steps = 70
print("You're on step:")
print(number_of_steps + 1)

private = 3
public = 10
total = private + public
print("Total posts:")
print(total)

# Divide to get average
sum_of_grades = 460
students = 5
print(sum_of_grades / students)

# Difference between string concatenation and numeric addition
area = "3 * 5"
print(area)        # prints the literal string "3 * 5" rather than 15

temperature_str = "3" + "1"
print(temperature_str)

# Subtract numbers
total = 100
discount = 20
print("Discounted price:")
print(total - discount)

# Reassign variable with new value
status = "Incomplete"
status = "Complete"
print(status)
status = "New data required"
print(status)

# Assign one variable from another
default_option = "upload"
new_status = "download"
new_status = default_option
print(new_status)
