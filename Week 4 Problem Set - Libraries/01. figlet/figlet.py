# install figelt
# import sys
# import figlet
# get user input
# checks sys args count
# check50 cs50/problems/2022/python/figlet

import sys

import random

from pyfiglet import Figlet

figlet = Figlet()


if len(sys.argv) >= 2:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font' or sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')

if len(sys.argv) == 1 :
    user_input = str(input('Input: '))
    font = figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(user_input))

elif len(sys.argv)  == 3:
    user_input = str(input('Input: '))
    font = figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(user_input))

