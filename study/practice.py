'''
The Task: Write a function process_email(email) that:Strips any whitespace.Converts it to lowercase.Splits the string at the @ symbol.Returns the result as a Tuple: (username, domain).
'''



emails = ["  Alice@Gmail.com ", "BOB@yahoo.COM", " charlie@Outlook.com "]

# precessed_email = [tuple(email.strip(" ").lower().split("@")) for email in emails]

def precess_email(email):
    result = tuple(email.strip(" ").lower().split("@"))
    return result

processed_email = [precess_email(e) for e in emails]

print(processed_email)