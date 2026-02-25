# Podmínky
# Podmínky nám umožňují řídit tok programu na základě určitých podmínek. Nejčastěji se používají příkazy if, elif a else.
# Syntaxe:
# if podmínka:
#     # blok kódu, který se vykoná, pokud je podmínka pravdivá
# elif další_podmínka:
#     # blok kódu, který se vykoná, pokud je další_pod
#     # podmínka pravdivá
# else:
#     # blok kódu, který se vykoná, pokud žádná z předchozích podmínek není pravdivá
# Příklad 1: Jednoduchá podmínka
x = 10
if x > 5:
    print("x je větší než 5")
# Příklad 2: Podmínka s elif a else
y = 15
if y < 10:
    print("y je menší než 10")
elif y == 10:
    print("y je rovno 10")
else:
    print("y je větší než 10")
# Příklad 3: Vnořené podmínky
z = 20
if z > 10:
    if z < 30:
        print("z je mezi 10 a 30")
    else:
        print("z je větší než nebo rovno 30")
else:
    print("z je menší než nebo rovno 10")

# Logické operátory
# Logické operátory nám umožňují kombinovat více podmínek. Nejčastěji používané logické operátory jsou and, or a not.
# Syntaxe:
# podmínka1 and podmínka2  # obě podmínky musí být pravdivé
# podmínka1 or podmínka2   # alespoň jedna podmínka musí být pravdivá
# not podmínka              # negace podmínky
# Příklad 1: Použití and
a = 5
b = 10
if a > 0 and b > 0:
    print("Obě čísla jsou kladná")
# Příklad 2: Použití or
c = -5
if a > 0 or c > 0:
    print("Alespoň jedno číslo je kladné")
# Příklad 3: Použití not
d = 0
if not d > 0:
    print("d není kladné číslo")  
