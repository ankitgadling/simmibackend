import random
from datetime import datetime
password = ""

def randomnumber():
    ascii_value = random.randint(48, 57)
    ascii_value2 = random.randint(48, 57)
    return chr(ascii_value)+chr(ascii_value2)

def randomcaptal():
    ascii_value = random.randint(65, 90)
    ascii_value2 = random.randint(65, 90)
    ascii_value3 = random.randint(65, 90)
    return chr(ascii_value)+chr(ascii_value2)+chr(ascii_value3)

def randomsmall():
    ascii_value = random.randint(65, 90)
    ascii_value2 = random.randint(65, 90)
    ascii_value3 = random.randint(65, 90)
    return chr(ascii_value)+chr(ascii_value2)+chr(ascii_value3)

def randosymbol():
    symbols = ["!","@","#","$","%","*"]
    symbol_id = random.randint(0, 5)
    symbol_id2 = random.randint(0, 5)
    return symbols[symbol_id]+symbols[symbol_id2]

def genarate_password():
    password = randomcaptal()+randomnumber()+randomsmall()+randosymbol()
    password_list=[]
    for char in password:
        password_list.append(str(char)) 
    random.shuffle(password_list)
    password = ''
    for char in password_list:
        password+=char
    return password


def get_name_from_email(email):
    name = ''
    for i in email:
        if i != "@":
            name += i
        else:
            break
    return name.capitalize()



