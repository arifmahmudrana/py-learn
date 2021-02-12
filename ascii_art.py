from pyfiglet import Figlet
from termcolor import cprint, COLORS
import enquiries


allowed_colors = list(COLORS.keys())
msg = input('Text you wanna print? ')
choice = enquiries.choose('Choose one of these colors: ', allowed_colors)

cprint(Figlet().renderText(msg), choice)
