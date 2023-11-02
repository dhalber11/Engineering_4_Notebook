#type: ignore
import board

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}
    FLASHES = {'.':'DOT', '-':'DASH'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier


Gled = digitalio.DigitalInOut(board.GP0)
Gled.direction = digitalio.Direction.OUTPUT

while True: 
    #print("Enter your Morse Code Message, or press -q to quit")
    Text = input("Enter your Morse Code Message, or press -q to quit:" )    #Ask for the users input
    if Text == "-q":    #if the kill code is entered
        print("Message ended")
        break                   # stop the program
    Up_text = Text.upper()      # turns the input to the same case
    for letter in Up_text:      # Takes each letter in the string and translates them one by one
        print(MORSE_CODE [f"{letter}"], end=" ")       # Print the output, "end =" puts them side by side
        
