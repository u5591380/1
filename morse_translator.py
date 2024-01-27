def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    text = text.upper()

    translated_text = []

    for char in text:
        if char.isalpha():
            if char in morse_code_dict:
                translated_text.append(morse_code_dict[char])
        elif char in [' ', '/']:
            translated_text.append(char)
            
    translated_text = ' '.join(translated_text)

    return translated_text





print(morse_translator("NISHIBUSHIDABENDAN?"))
