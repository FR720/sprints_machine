# Requirement 1 

# Step 1: Create a list of integers
integer_list = [10, 20, 30, 40, 50]
print("Initial list:", integer_list)

# Step 2: Add new elements
integer_list.append(60)
integer_list.extend([70, 80])
print("List after adding elements:", integer_list)

# Step 3: Remove an element
integer_list.remove(30)
print("List after removing an element (30):", integer_list)

# Step 4: Access specific elements
second_element = integer_list[1]
last_element = integer_list[-1]
print("Second element:", second_element)
print("Last element:", last_element)

#################################################################
# Requirement 2 

# Step 1: Create a tuple of strings
tuple_of_strings = ("apple", "banana", "cherry", "date")
print("Tuple of strings:", tuple_of_strings)

# Step 2: Access elements of the tuple
first_item = tuple_of_strings[0]
last_item = tuple_of_strings[-1]
print("First item in tuple:", first_item)
print("Last item in tuple:", last_item)

# Step 3: Create a set of integers
integer_set = {10, 20, 30, 40}
print("Initial set:", integer_set)

# Step 4: Add elements to the set
integer_set.add(50)
integer_set.update([60, 70])
print("Set after adding elements:", integer_set)

# Step 5: Perform union and intersection operations
another_set = {30, 40, 70, 80}
union_result = integer_set.union(another_set)
intersection_result = integer_set.intersection(another_set)
print("Union of sets:", union_result)
print("Intersection of sets:", intersection_result)


#################################################################
# Requirement 3 

# Step 1: Create a dictionary
dictionary = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print("Initial dictionary:", dictionary)

# Step 2: Add a new key-value pair
dictionary["profession"] = "Engineer"
print("Dictionary after adding a new key-value pair:", dictionary)

# Step 3: Modify an existing key-value pair
dictionary["age"] = 26
print("Dictionary after modifying the 'age' key:", dictionary)

# Step 4: Access specific key-value pairs
name = dictionary["name"]
city = dictionary.get("city")
print("Name:", name)
print("City:", city)
