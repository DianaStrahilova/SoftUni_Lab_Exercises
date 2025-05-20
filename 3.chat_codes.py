number_of_messages = int(input())


for message in range(number_of_messages):
    current_message = int(input())
    current_reply = ""

    if current_message == 88:
        current_reply = "Hello"
    elif current_message == 86:
        current_reply = "How are you?"
    elif current_message < 88:
        current_reply = "GREAT!"
    else:
        current_reply = "Bye."

    print(current_reply)

