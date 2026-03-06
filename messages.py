"""
8-9
Messages 
Make a list containing series of short text message. Pass the lsit to a function called show_messages(), which prints
each text message.
"""
message = ['hey','hey','did i miss anything important on our programming class', 'bro you should really stop skipping that class','i knowww im just horrible at waking up :(']
def show_messages(list):
    for text in list:
        print(f'{text}\n')
show_messages(message)
