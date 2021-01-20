print("This is not a comment")  # This is a single line comment
print("It automatically prints a new line")  # Ohh
"""
This is a
Multi-line comment
"""

print("This will stop the addition of any new line", end=" ")  # Fill end of line with a space
print("This will stop the addition of any new line", end="")  # Fill end of line with a blank
print("Now no new line is here")

# We can also use only one print statement for this
print("This is printed","With only one print statement")

# Escape sequences are same as in C Language
print("This\tis\na test for the escape\bE sequence characters", end=" #LEGEND")