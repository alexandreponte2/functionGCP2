from requests import get
import base64
import json
import re
from google.cloud.sql.connector import Connector
import sqlalchemy
from google.cloud import secretmanager
from random import choice
import string
from os import getenv


###Filtrar os dados:
#PROJECT_ID = getenv("PROJECT_ID")

TOKEN = getenv("TOKEN")
ENVIROMENT = getenv("ENVIROMENT")
PRODUCT = getenv("PRODUCT")
URL_API = getenv("URL_API")
HEADERS = {'Authorization': (TOKEN)}

def get_secret_list():
    r = get(
        f'{URL_API}/{PRODUCT}/{ENVIROMENT}/?refresh=1', headers=HEADERS)
    return r.json()


apireturn =  get_secret_list()

get_secret_list()

print(apireturn)




# old



# import base64
# import json
# import re
# from os import getenv


# PROJECT_ID = getenv("PROJECT_ID")
# SECRET_ID  = getenv("SECRET_ID")

# def echo_teste():
#  print (PROJECT_ID)
#  payload = PROJECT_ID
#  return payload



# senha = echo_teste()
# print(format(senha))

# secret = SECRET_ID

# print(secret)