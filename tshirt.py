"""
8-3 
T-Shirt
Write a function called make_shirt() that accepts a size and the text of a message that should be printed
on the shirt. The functio  should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
def make_shirt(size='l', message='I love python'):
    print(f"A shirt of size {size.upper()} will have the following message printed on it:\n{message}")

make_shirt('l')
make_shirt('m')
make_shirt('s','Programming is fun')

"""
8-4 
Large shirts
Modify the make_shirt() function so that shirts are large by default with a message that reads "I love python".
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""
