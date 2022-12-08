import base64
import json
import re
from os import getenv


PROJECT_ID = getenv("PROJECT_ID")
SECRET_ID  = getenv("SECRET_ID")

def echo_teste():
 print (PROJECT_ID)
 payload = PROJECT_ID
 return payload



senha = echo_teste()
print(format(senha))

secret = SECRET_ID

print(secret)