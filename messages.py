"""
8-9
Messages 
Make a list containing series of short text message. Pass the lsit to a function called show_messages(), which prints
each text message.
"""
def show_messages(list):
    for text in list:
        print(f'{text}\n')
def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"Sending:\n{message}\n")
        sent_messages.append(message)
        

messages = ['hey','hey','did i miss anything important on our programming class', 'bro you should really stop skipping that class','i knowww im just horrible at waking up :(']
sent_messages = []

show_messages(messages)

send_messages(messages, sent_messages)

show_messages(messages)
show_messages(sent_messages)


"""
8-10
Building on excerice 8-9, write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it's printed.
 After calling the functionm print bith of your lists to make sure the messages were moved correctly""" 