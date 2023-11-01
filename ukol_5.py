# Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech
# - ráno, v poledne, večer a v noci.

# 1. Vytvoř seznam průměrných teplot pro každý den.
# 2. Vytvoř seznam ranních teplot.
# 3. Vytvoř seznam nočních teplot.
# 4. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.


import statistics

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerna = [statistics.mean(den) for den in teploty]
print("Průměrné:", prumerna)

ranni = [den[0] for den in teploty]
print("Ranní:", ranni)

nocni= [den[-1] for den in teploty]
print("Noční:", nocni)

poledni_a_nocni = [[den[1], den[-1]] for den in teploty]
print("Polední a noční:", poledni_a_nocni) 

# BONUS
# Pomocí dict comprehension vytvoř slovník, který bude mít následující formát,
# kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.
# {den: průměrná teplota} 

teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

nove_teploty = {den[0]: sum(den[1:]) / len(den[1:]) for den in teploty}
print(nove_teploty)