

# Soubor si ulož a načti do slovníku.
# Z písemky nebude známka,
# ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a).
# Vytvoř nový slovník. Jeho klíče budou opět jména žáků,
# a hodnotou bude řetězec "Pass",
# pokud má jednotlivec alespoň než 60 bodů.
# Pokud má méně než 60, hodnota bude "Fail".

# Výsledný slovník ulož jako JSON do souboru prospech.json.

import json
with open("body.json", mode="r", encoding='utf-8') as soubor:
    studenti = json.load(soubor)

prospech = {}

for name, value in studenti.items():
    if value >= 60:
        prospech[name] = "Pass"
    else:
        prospech[name] = "Fail"

with open("prospech.json", mode="w", encoding="utf-8") as soubor:
    json.dump(prospech, soubor, ensure_ascii=False, indent=4)


