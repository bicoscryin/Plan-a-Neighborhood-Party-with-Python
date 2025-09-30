import datetime
secret_message = input("What is your secret message? ")
send_time = str(datetime.datetime.now())
recipient = input("Who is this message intended for? ")

#Strip extra spaces
secret_message = secret_message.strip()
recipient = recipient.strip()
print(f"Secret message: {secret_message}\nRecipient: {recipient}")

#message transformation
secret_message = " \nThis message was sent at: ".join([secret_message,send_time])
uppercase_message = secret_message.upper()
clean_message = secret_message.capitalize()
reverse_message = secret_message[::-1]

#Name transmforation
separate_recipient_name = recipient.split(" ")
clean_recipient = []
for word in separate_recipient_name:
    clean_recipient.append(word.capitalize())
clean_recipient = " ".join(clean_recipient)
x = "x"

#Menu
print(f"Hello, {clean_recipient}. Please select the delivery method of your message:")
print("1: Reverse\n2: Uppercase\n3: Cleane message")
option = int(input("Which number would you like to see? "))
#while 1 < option > 3 and option != 42 :
if option == 1:
     print(reverse_message)
elif option == 2:
     print(uppercase_message)
elif option == 3:
     print(clean_message)
elif option == 42:
     print(f"You have revealed all secrets:\n{reverse_message}\n{uppercase_message}\n{clean_message}")
else:
     option = int(input(f"{option} was not one of your choices. Please select an option: "))