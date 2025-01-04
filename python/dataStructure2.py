# Requirement 1 
# Step 1: Create a dictionary to store student records
student_records = {}

# Step 2: Functions to add, update, and retrieve student records
def add_student(name, age, grades):
    student_records[name] = {
        "age": age,
        "grades": grades
    }
    print(f"Added student: {name}")

def update_student(name, age=None, grades=None):
    if name in student_records:
        if age is not None:
            student_records[name]["age"] = age
        if grades is not None:
            student_records[name]["grades"] = grades
        print(f"Updated student: {name}")
    else:
        print(f"Student {name} not found.")

def retrieve_student(name):
    return student_records.get(name, f"Student {name} not found.")

 
add_student("Alice", 20, [85, 90, 78])
add_student("Bob", 22, [92, 88, 84])
update_student("Alice", grades=[88, 91, 80])
print("Retrieve Alice's record:", retrieve_student("Alice"))

#################################################################


# Requirement 2 
# Step 1: Create a set to track unique items in a shopping cart
shopping_cart = set()

# Step 2: Functions to add and remove items
def add_item(item):
    shopping_cart.add(item)
    print(f"Added item: {item}")

def remove_item(item):
    if item in shopping_cart:
        shopping_cart.remove(item)
        print(f"Removed item: {item}")
    else:
        print(f"Item {item} not found in the cart.")

 
add_item("apple")
add_item("banana")
add_item("apple")   
remove_item("banana")
print("Current shopping cart:", shopping_cart)


#################################################################
# Requirement 3 

# Step 1: Create a tuple for fixed configuration data
CONFIG = ("MAX_USERS", 1000, "API_KEY", "12345-ABCDE", "DATABASE_URL", "https://db.example.com")

 
print("Configuration data:", CONFIG)
