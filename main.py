from playsound import playsound
import time

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}
user_text = input('Type text to convert to morse code: ').upper()

# answer = ''
# for letter in user_text:
#     answer = answer + MORSE_CODE_DICT[letter] + " "

x = [MORSE_CODE_DICT[letter] for letter in user_text]
answer = ' '.join(x)
print(answer)
for morse in x:
    for piece in morse:
        if piece == '-':
            playsound('C:/Users/micha/PycharmProjects/texttomors/long-morse.mp3')
        elif piece == ".":
            playsound('C:/Users/micha/PycharmProjects/texttomors/short-morse.mp3')
        #BETWEEN PIECES
        time.sleep(0.1)
    #TIME SLEEP BETWEEN LETTERS
    time.sleep(0.5)
