# Cyklus while
# Opakuje dokud platí podmínka
# Syntaxe:
# while podmínka:
#     # blok kódu, který se opakuje, dokud je podmín
# podmínka může být jakýkoli výraz, který se vyhodnotí jako True nebo False nebo čístě logický výraz
# Příklad 1: Počítadlo
i = 0
while i < 5:
    print(i)
    i += 1  # zvyšujeme i o 1, aby se cyklus nakonec zastavil
# Příklad 2: Nekonečný cyklus (pozor, může způsobit zamrznutí programu)
# while True:
#     print("Toto se bude opakovat navždy!")
# Příklad 3: Použití break pro ukončení cyklu
j = 0
while j < 10:
    print(j)
    if j == 5:
        break  # ukončí cyklus, když j dosáhne 5
    j += 1
# Příklad 4: Použití continue pro přeskočení aktuální iterace
k = 0
while k < 10:
    k += 1
    if k % 2 == 0:
        continue  # přeskočí zbytek kódu pro sudá čísla
    print(k)  # vytiskne pouze lichá čísla
