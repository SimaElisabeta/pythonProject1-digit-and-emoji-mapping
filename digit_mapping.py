digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

# the variable phone will receive from input a string of characters
phone = input("Write your phone number: ")

# for each character received from my input
# digits_mapping.get(char) will receive a character (the char is the key) and will get the value from it
# print the value: char is key, and value is the value attributed to it from my digits_mapping
for char in phone:
    print(digits_mapping.get(char, "??"), end=" ")
