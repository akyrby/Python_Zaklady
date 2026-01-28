# Datové typy v Pythonu

# 1. String (řetězec) - textový datový typ
text = "Ahoj, světe!"
print("Text:", text)
print("Typ textu:", type(text))
# Operace s řetězci
delka_textu = len(text)
print("Délka textu:", delka_textu)
prvni_pismeno = text[0]
print("První písmeno:", prvni_pismeno)
podretezec = text[0:5] # Ahoj,
print("Podřetězec:", podretezec)
text_velka = text.upper()
print("Text velkými písmeny:", text_velka)
text_mala = text.lower()
print("Text malými písmeny:", text_mala)
text_nahrazeni = text.replace("světe", "Python")
print("Nahrazený text:", text_nahrazeni)

# 2. Integer (celé číslo) - numerický datový typ
cele_cislo = 42
print("Celé číslo:", cele_cislo)
print("Typ celého čísla:", type(cele_cislo))
# Operace s celými čísly
soucet = cele_cislo + 10
print("Součet:", soucet)
rozdil = cele_cislo - 5
print("Rozdíl:", rozdil)
soucin = cele_cislo * 2
print("Součin:", soucin)
podil = cele_cislo // 3
print("Podíl (celé číslo):", podil)
zbytek = cele_cislo % 7
print("Zbytek po dělení:", zbytek)

# 3. Float (desetinné číslo) - numerický datový typ
desetinne_cislo = 3.14
print("Desetinné číslo:", desetinne_cislo)
print("Typ desetinného čísla:", type(desetinne_cislo))
# Operace jsou stejné jako u celých čísel

# 4. Boolean (pravda/nepravda) - logický datový typ
pravda = True
nepravda = False
print("Pravda:", pravda)
print("Typ pravdy:", type(pravda))
print("Nepravda:", nepravda)
print("Typ nepravdy:", type(nepravda))
# Operace s booleany
a_logicky = pravda and nepravda
print("A logický:", a_logicky)
nebo_logicky = pravda or nepravda
print("Nebo logický:", nebo_logicky)
negace = not pravda
print("Negace pravdy:", negace)

# Převod mezi datovými typy
# String na Integer
str_cislo = "100"
int_cislo = int(str_cislo)
print("Převedené číslo (string na int):", int_cislo)