# Úkol 2

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadejte kód součástky: ")

if kod not in sklad:
    print("Součástka není skladem")

mnozstvi = input("Zadejte množství: ")
mnozstvi = int(mnozstvi)

mnozstvi_ve_skladu = sklad[kod]

if mnozstvi > mnozstvi_ve_skladu:
        print("Lze prodat jen omezené množství")

        del sklad[kod]

        print("Kontrola stavu skladu:")
        print(sklad)

if mnozstvi_ve_skladu > mnozstvi:
        print("Poptávku lze uspokojit v plné výši")

        sklad[kod] = mnozstvi_ve_skladu-mnozstvi

        print("Kontrola stavu skladu:")
        print(sklad)


# Nepovinný bonus 1

morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}


text = input("Zadejte text pro převod: ")

for znaky in text:
    
    if " " in znaky:
        morse_code[" "] = "/"

    print(morse_code[znaky], end=" ")