'''
Problem 1: The "Email Validator" (Cleaning & Tuples)
The Scenario: You have a list of raw user inputs. You need to separate the Username from the Domain and return them as a "locked" pair.
The Task: Write a function process_email(email) that:Strips any whitespace.Converts it to lowercase.Splits the string at the @ symbol.Returns the result as a Tuple: (username, domain).
'''
# solution 1.0

email_list = ["user1@gmail.com", "user2@yahoo.com", "user3@outlook.com"]  

def process_email(email):
    cleaned = email.strip(" ").lower()
    username, domain = cleaned.split("@")
    return (f"username: {username}", f"domain: {domain}")

result = tuple(process_email(e) for e in email_list)
# result = [process_email(e) for e in email_list]
print(result)

# solution 1.1
def process_mail(email):
    validated_email = ()
    for e in email:
        validated_email += (tuple(e.strip(" ").lower().split("@")),)
    return validated_email

print(process_mail(email_list))

# solution 1.2

def processs_email(email):
    return(
        tuple(
            tuple(
                e.strip(" ").lower().split("@")) for e in email
        )
    )

print(processs_email(email_list))

'''
Problem 2: The "Data Masker" (List Comp & Slicing)
The Scenario: You have a list of credit card numbers (strings). For security, you need to hide all numbers except the last 4.
The Task: Use a List Comprehension to take a list of 16-digit strings and turn them into "masked" versions where the first 12 digits are * and the last 4 are visible.
cards = ["1234567812345678", "9876543298765432", "1111222233334444"]
'''
# solution 2.0
cards = ["1234567812345678", "9876543298765432", "1111222233334444"]

masked_cards = ["*"*len(num[:-4])+num[-4:] for num in cards]
print(masked_cards)

'''
Problem 3: The "Inventory Analyzer" (Everything Combined)
The Challenge: You are given a list of product strings in this format: "itemName:Price".
Example: ["Laptop:1000", "Mouse:25", "Monitor:300"]
The Task: Write a script that:Uses a List Comprehension to turn that list into a list of Tuples: [("Laptop", 1000), ...]. (Hint: You'll need to split(":") and convert the price to an int).
Uses the max() and min() functions on the prices to find the most expensive and cheapest items.

raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]
'''
# solution 3.0
raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]

inventory = [(item, int(price)) for item, price in (entry.split(":") for entry in raw_inventory)]
most_expensive_item = max(inventory, key= lambda product: product[1])
cheapest_item = min(inventory, key= lambda product: product[1])

print("Inventory:", inventory)
print("Most expensive item", most_expensive_item)
print("Cheapest item", cheapest_item)



