# Datové struktury (Data Structures)
# List, Tuple, Set, Dictionary

# List (Seznam)
# Seznam je uspořádaná, měnitelná kolekce prvků, která umožňuje duplicitní hodnoty.
# Prvky jsou indexovány od nuly, neboli každý prvek má své pořadové číslo.
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
my_list.append(6)
print("Po přidání 6:", my_list)
my_list.remove(2)
print("Po odstranění 2:", my_list)
print("První prvek seznamu:", my_list[0])
print("Délka seznamu:", len(my_list))
# Operace se seznamy:
# Přidání prvku: append(), insert()
my_list.append(7) # přidá na konec
my_list.insert(0, 0) # 1. číslo je index, 2. číslo je hodnota
print("Po přidání 0 na začátek a 7 na konec:", my_list)
# Odstranění prvku: remove(), pop()
my_list.remove(3) # odstraní první výskyt hodnoty 3
popped_value = my_list.pop() # odstraní a vrátí poslední prvek
print("Po odstranění prvku 3 a posledního prvku:", my_list)
print("Odstraněná hodnota:", popped_value)
# Přístup k prvkům: indexování, slicing
first_element = my_list[0]
sliced_list = my_list[1:4] # prvky od indexu 1 do 3
print("První prvek:", first_element)
print("Výřez seznamu (index 1 až 3):", sliced_list)

print("*" * 40)



# Tuple (N-tice)
# N-tice je uspořádaná, neměnitelná kolekce prvků, která umožňuje duplicitní hodnoty.
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("První prvek n-tice:", my_tuple[0])
# Operace s n-ticemi:
# Přístup k prvkům: indexování, slicing
first_element_tuple = my_tuple[0]
sliced_tuple = my_tuple[1:4] # prvky od indexu 1 do 3
print("První prvek n-tice:", first_element_tuple)
print("Výřez n-tice (index 1 až 3):", sliced_tuple)

print("*" * 40)

# Set (Množina)
# Množina je neuspořádaná, neměnitelná kolekce unikátních prvků.
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
my_set.add(6)
print("Po přidání 6:", my_set)
my_set.remove(2)
print("Po odstranění 2:", my_set)
print("Obsahuje 3?", 3 in my_set)
# Operace s množinami:
# Přidání prvku: add()
my_set.add(7)
print("Po přidání 7:", my_set)
# Odstranění prvku: remove(), discard()
my_set.remove(4) # odstraní prvek 4
my_set.discard(10) # nevyvolá chybu, pokud prvek neexistuje
print("Po odstranění 4 a pokusu o odstranění 10:", my_set)
# Operace množin: union(), intersection(), difference()
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
difference_set = set_a.difference(set_b)
print("Sjednocení:", union_set)
print("Průnik:", intersection_set)
print("Rozdíl (A - B):", difference_set)

print("*" * 40)

# Dictionary (Slovník)
# Slovník je neuspořádaná, měnitelná kolekce párů klíč-hodnota.
my_dict = {'jméno': 'Alice', 'věk': 25, 'město': 'Praha'}
print("Dictionary:", my_dict)
my_dict['věk'] = 26
print("Po změně věku na 26:", my_dict)
del my_dict['město']
print("Po odstranění města:", my_dict)
print("Jméno:", my_dict['jméno'])
# Operace se slovníky:
# Přidání/změna páru klíč-hodnota
my_dict['povolání'] = 'Inženýr'
print("Po přidání povolání:", my_dict)
# Odstranění páru klíč-hodnota: del, pop()
del my_dict['věk']
popped_value_dict = my_dict.pop('jméno')
print("Po odstranění věku a jména:", my_dict)
print("Odstraněné jméno:", popped_value_dict)
# Přístup k hodnotám pomocí klíčů
city = my_dict.get('město', 'Neznámé město')
print("Město:", city)
# Získání všech klíčů a hodnot: keys(), values()
keys = my_dict.keys()
values = my_dict.values()
print("Klíče:", keys)
print("Hodnoty:", values)

