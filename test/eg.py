# def days(original_function):
#     def wrapper_function(*args, **kwargs):
#         if args == 0: return "Monday"
#         elif args == 1: return "Tuesday"
#         elif args == 2: return "Wednesday"
#         elif args == 3: return "Thursday"
#         elif args == 4: return "Friday"
#         elif args == 5: return "Saturday"
#         elif args == 6: return "Sunday"
#         return original_function(*args, **kwargs)
#     return wrapper_function

def days(args):
    if args == 0: return "Monday"
    elif args == 1: return "Tuesday"
    elif args == 2: return "Wednesday"
    elif args == 3: return "Thursday"
    elif args == 4: return "Friday"
    elif args == 5: return "Saturday"
    else: return "Sunday"
  
