# This small line of code helps you store sensitive info on your system 
# environ folder and pull it out whenever neccesary, its the same as env func

import os

email = os.environ.get('POSTGRES_PASSWORD')
# print(os.environ.get("API_KEY"))
print(email)