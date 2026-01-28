# Deklarace proměnných

jmeno = "Jan" # String (řetězec)
prijmeni = "Novák" # String (řetězec)
vek = 25 # Integer (celé číslo)
vyska = 1.75 # Float (desetinné číslo)
je_student = True # Boolean (pravda/nepravda)
# nebo
jmeno, prijmeni, vek = "Jan", "Novák", 25

# Taky lze zapsat prázdné pomněnné
adresa = str() # prázdný řetězec
cislo = int() # nula
telefon = None # None znamená, že proměnná nemá žádnou hodnotu



# Při vytváření proměnných je důležité dodržovat pravidla:
# 1. Název proměnné musí začínat písmenem nebo podtržítkem (_)
# 2. Název proměnné nesmí obsahovat mezery ani speciální znaky (kromě podtržítka)
# 3. Název proměnné by měl být výstižný a popisný (příklad: vek místo vek123)
# 4. Proměnné jsou case-sensitive (rozlišují velká a malá písmena)
# 5. Názvy proměnných nesmí být klíčová slova jazyka Python (např. if, for, while, atd.)
# 6. Pro více slov v názvu proměnné se doporučuje používat podtržítka (např. celkovy_vek)

# Výpis hodnot proměnných
print("Jméno:", jmeno)
print("Příjmení:", prijmeni)
print("Věk:", vek)
print("Výška:", vyska)
print("Je student:", je_student)
# Výpis typu proměnných pomocí funkce type()
print("Typ jmeno:", type(jmeno))
print("Typ vek:", type(vek))
print("Typ vyska:", type(vyska))
print("Typ je_student:", type(je_student))

# Formátovaný výpis pomocí f-string
print(f"{jmeno} {prijmeni} je {vek} let starý/á, jeho/její výška je {vyska} m a je student: {je_student}")
# Formatovaný výpis - f-string umožnuje vkládat proměnné přímo do řetězce pomocí složených závorek {}
# když chceme využít f-string, musíme před řetězec napsat písmeno f nebo F, následně uvozovky nebo apostrofy a uvnitř pak můžeme používat složené závorky {}, ve kterých budou názvy proměnných, jejichž hodnoty chceme do řetězce vložit.
# Příklad:
print(f"Ahoj, jmenuji se {jmeno} {prijmeni}, je mi {vek} let.")
