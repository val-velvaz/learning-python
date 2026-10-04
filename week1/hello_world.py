"""
Make a simple function called greet that returns the 
most-famous "hello world!".

Style Points
Sure, this is about as easy as it gets. But how 
clever can you be to create the most creative 
"hello world" you can think of? What is a "hello 
world" solution you would want to show your friends?
"""

def greet():
    s = b"\x48\x45\x4C\x4C\x4F\x20\x57\x4F\x52\x4C\x44\x21"
    return s.decode('ascii').lower()

greet()