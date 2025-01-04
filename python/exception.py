# Requirement 1 

def get_number():
    """
    Asks the user for a number and handles invalid input using try/except.
    """
    try:
        number = int(input("Enter a number: "))
        print(f"You entered: {number}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

 
get_number()



#################################################################
# Requirement 2 

class AgeError(Exception):
    """
    Custom exception raised for invalid age values.
    """
    pass

def validate_age(age):
    """
    Validates the age and raises AgeError for invalid values.
    """
    if age < 0 or age > 120:
        raise AgeError("Age must be between 0 and 120.")
    print(f"Valid age: {age}")


try:
    validate_age(130)
except AgeError as e:
    print(e)


#################################################################
# Requirement 3 

def process_file(file_path):
    """
    Demonstrates the use of finally and else clauses in exception handling.
    """
    try:
        file = open(file_path, 'r')
        print("File opened successfully.")
        content = file.read()
    except FileNotFoundError:
        print("File not found.")
    else:
        print("File content:", content)
    finally:
        if 'file' in locals() and not file.closed:
            file.close()
            print("File closed.")


process_file("test.txt")
