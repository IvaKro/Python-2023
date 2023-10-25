# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv.
# Napiš program, který provede následující činnosti:

# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné
# nebo třináctimístné (pokud je na začátku předvolba "+420").
# Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True,
# jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla.
# Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy
# a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce.
# Ty porovnejte s řetězcem "+420".

from math import ceil

print ("**APLIKACE PRO ZASÍLÁNÍ SMS**")

def correct_number(number):
    if len(number) == 9 or len(number) == 13 and (number[:4]) == "+420":
        return True
    else:    
         return False

def price(message):
    length = len(message)
    x = ceil(length/180)
    total_price = x * 3
    return total_price
    

number = input ("Na jaké číslo chceš zaslat SMS?: ")


if correct_number(number):
    message = input("Cena SMS je 3 Kč za každých započatých 180 znaků. Napište zprávu: ")
    total_price = price(message)
    print("Cena zprávy je", (total_price), "Kč.")
else:
    print("Špatný formát telefonního čísla.")


