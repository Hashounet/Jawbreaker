# -*- coding: utf-8 -*-


# GLOBALS DICT

from base64 import b16encode, b32encode, b64encode, b16decode, b32decode, b64decode
from builtins import *

globals_names = {k:v for k,v in globals().items()}


# REQUIREMENTS

from pyfade import Colors, Fade
from pycenter import center
from requests import post

from random import randint, choice
from sys import argv
from os.path import isfile
from os import name, system


def clear():
    system("cls" if name == 'nt' else "clear")

clear()



if name == 'nt':
    system("title Jawbreaker")
    system("mode 160, 40")

encoding = 'utf-8'
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ignore = ("b16encode", "b32encode", "b64encode")


class Col:
    colors = {"red" : "\033[38;2;255;0;0m", 
              "green" : "\033[38;2;0;255;0m", 
              "blue" : "\033[38;2;0;0;255m",
              "white" : "\033[38;2;255;255;255m"}

    red = colors['red']

    green = colors['green']

    blue = colors['blue']

    white = colors['white']

class Create():
        def __init__(self):
            self.content= ""
        def write(self, content):
            self.content += content





jawbreaker = """
       #                                                                
       #   ##   #    # #####  #####  ######   ##   #    # ###### #####  
       #  #  #  #    # #    # #    # #       #  #  #   #  #      #    # 
       # #    # #    # #####  #    # #####  #    # ####   #####  #    # 
 #     # ###### # ## # #    # #####  #      ###### #  #   #      #####  
 #     # #    # ##  ## #    # #   #  #      #    # #   #  #      #   #  
  #####  #    # #    # #####  #    # ###### #    # #    # ###### #    # 
                                                                        
"""

author = "  # # # {} # # #".format(b64decode("YmlsbHl0aGVnb2F0MzU2").decode('utf-8'))

print(Fade.Vertical(Colors.blue_to_cyan, center(jawbreaker)))
print(Fade.Horizontal(Colors.cyan_to_green, center(author)))

print("\n")

if len(argv) > 1:
    file = argv[1]
    print(Col.green+"Enter file name > "+Col.white+file)
else:
    file = input(Col.green+"Enter file name > "+Col.white)

if not isfile(file):
    print()
    input(Col.red+"This file doesn't exists!"+Col.white)
    exit()

if len(argv) > 2:
    output = argv[2]
    print(Col.green+"Enter name of output file > "+Col.white+output)
else:
    output = input(Col.green+"Enter name of output file > "+Col.white)


    
print()
print("Building obfuscated file...")


def nfile(file:object, only:bool=False) -> tuple:
    
    temp_names = ["exec", "b16decode", "b32decode", "b64decode"] if only else [name for name in globals_names]

    for name in temp_names:
        random_name = random()
        if name == "exec":
            exc = random_name
        elif name == "b16decode":
            file.write(f"from base64 import b16decode as {random_name};")
            b16 = random_name
            continue
        elif name == "b32decode":
            file.write(f"from base64 import b32decode as {random_name};")
            b32 = random_name
            continue
        elif name == "b64decode":
            file.write(f"from base64 import b64decode as {random_name};")
            b64 = random_name
            continue
        elif name in ignore:
            continue
        file.write(f"{random_name} = {name};")
    return exc, b16, b32, b64

def random(l:int=2) -> str:
    return "".join(choice(chars) + choice([choice(chars), str(randint(0,9))]) for _ in range(1, l+1))
    

def build():

    with open(file, 'r', encoding=encoding) as f:
        content = f.read()


    key = post("https://hastebin.com/documents", data=content.encode('utf-8')).json()["key"]
    url = "https://hastebin.com/raw/" + key



    file_1 = Create()

    exc, b16, b32, b64 = nfile(file_1)

    urlp = random()
    req = random()
    file_1.write(f"from urllib.request import urlopen as {urlp}, Request as {req};")

    chars_list = random()
    file_1.write(f"{chars_list}=[];")
    content = f"""{exc}({urlp}({req}("{url}", headers={{"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}})).read())"""

    content = b16encode(b32encode(b64encode(content.encode(encoding)))).decode(encoding)

    random_chars_list = []

    for char in content:
        random_char = random()
        random_chars_list.append(random_char)
        file_1.write(f"{random_char}='{char}';")

    random_append_function = random()
    file_1.write(f"{random_append_function}={chars_list}.append;")

    for random_char in random_chars_list:
        file_1.write(f"{random_append_function}({random_char});")

    content_name = random()
    file_1.write(f"{content_name} = ''.join({chars_list});")
 

    file_1.write(f"{exc}({b64}({b32}({b16}({content_name}))));")



    content = file_1.content
    
    content = b16encode(b32encode(b64encode(content.encode(encoding)))).decode(encoding)


    file_2 = Create()


    exc, b16, b32, b64 = nfile(file_2)

    file_2.write(f'{exc}({b64}({b32}({b16}("{content}"))));')

    content = file_2.content

    with open(output, 'w', encoding=encoding) as f:
        f.write(content)



try:
    build()
    input(Col.blue+"Done!"+Col.white)
except Exception as e:
    input(Col.red+"Error! [{}]".format(e)+Col.white)