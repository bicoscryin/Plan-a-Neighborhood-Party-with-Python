secret_message = input("What is your secret message?")
recipient = input("Who is this message intended for?")

#Strip extra spaces
secret_message = secret_message.strip()
recipient = recipient.strip()
print(f"Secret message: {secret_message}\nRecipient: {recipient}")

#message transformation
uppercase_message = secret_message.upper()
print("This is upper", uppercase_message)
clean_message = secret_message.capitalize()
print("This is cleaned up ", clean_message)
reverse_message = secret_message[6:0]
print("This is mixed up ", reverse_message)