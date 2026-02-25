# For cyklus
# Slouží k iteraci (procházení) přes sekvence (jako jsou seznamy, n-tice, řetězce) nebo jiné iterovatelné objekty.
# Syntaxe:
# for proměnná in sekvence:
#     # blok kódu, který se opakuje pro každý prvek v sekvenci
# Příklad 1: Iterace přes seznam
ovoce = ["jablko", "banán", "třešeň"]
for plod in ovoce:
    print(plod)
# Příklad 2: Iterace přes řetězec
slovo = "Python"
for písmeno in slovo:
    print(písmeno)
# Příklad 3: Použití funkce range() pro iteraci přes čísla
for i in range(5):
    print(i)
for i in range(1, 10, 2): # iterace od 1 do 9 s krokem 2
    print(i)
# Příklad 4: Iterace přes seznam s indexy pomocí funkce enumerate()
seznam = ["a", "b", "c"]
for index, hodnota in enumerate(seznam):
    print(f"Index: {index}, Hodnota: {hodnota}")