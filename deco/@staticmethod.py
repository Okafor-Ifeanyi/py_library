# Check @classmethod.py for more info
# Staticmethod much like class methods are methods that are bound to a class rather than its object 
# They don't require a class instance creation. So they are not dependent on the state of the object.
# The difference between a static method and a class method is:
#   Static method knows nothing about the class and just deals with the parameters
#   Class method works with the class since its parameter is always the class itself

# When are they used
# Generally they are useful to group utility functions to a class.

import time

class Hour:
    def __init__(self, seconds):
        self.seconds = seconds
    
    @staticmethod
    def convert_seconds_to_hour(seconds):
        return time.strftime("%H:%M:%S", time.gmtime(seconds))

    def display_hour(self):
        hour = self.convert_seconds_to_hour(self.seconds)
        return f"The Hour is {hour}"

oge = Hour(300)
print(oge.display_hour())