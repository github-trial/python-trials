import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def colour_print(text: str, effects: str) -> None:
   """
   Print `text` using the ASCI sequences to change colour, etc

   :param text: The text to colour_print
   :param effects: The effect we want:  One of the constants defined
     at the start of this module.
   """
   output_string = "{0}{1}{2}".format(effects, text, RESET)
   print(output_string)

colorama.init()
colour_print("Hello, World", RED)
colour_print("Hello, World", RED)
colour_print("Hello, World", BLUE)
colour_print("Hello, World", REVERSE)
colour_print("Hello, World", BOLD)
colour_print("Hello, World", BLACK)
colour_print("Hello, World", WHITE)
colour_print("Hello, World", CYAN)
colour_print("Hello, World", RESET)
colour_print("Hello, World", UNDERLINE)
colorama.deinit()



