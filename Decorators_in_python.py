# # TAKING FUCNTION AS AN ARGUMENT
# def excecutor(func):
#     func("Legend: ")


# excecutor(print)
# excecutor(input)


# CONCEPT OF DECORATORS

def decorator(func):
    def now_execute():
        print("Starting execution...")
        func()
        print("Completed!!")
    return now_execute


# ALTERNATIVE OF WRITING: sample_function = decorator(sample_function)
@decorator
def sample_function():
    print("This is a sample function")


# sample_function = decorator(sample_function)
sample_function()  # Calling the final function
