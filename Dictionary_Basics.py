my_dict = {
    "brand": "Hyundai",
    "model": "GrandI10",
    "year": 2019
}

# following will give key error:
# print(my_dict["Type"])
# Error --> KeyError: 'Type'

# Always use get method as it returns None if key doesn't exist
print(my_dict.get("Type"))

# To add key
my_dict["Type"] = "Car"

# To delete use pop(Key_name), popitem() will remove any random key value pair
# Delete dictionary --> del dictionary_name

# Dictionary Comprehension

my_dict = {
    1: "Hyundai",
    2: "GrandI10",
    3: "2019"
}
#Get all values where key is greater than equal to 2

new_dict = { k: v for k, v in my_dict.items() if k >= 2 }
print(new_dict)