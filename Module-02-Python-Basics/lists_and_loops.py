# 1. Lista produktów na stronie
products = ["Backpack", "Bike Light", "Bolt T-Shirt", "Onesie"]

# 2. Lista produktów, które są aktualnie w magazynie
available_products = ["Backpack", "Bolt T-Shirt"]

print("--- Raport dostępności produktów ---")

# MOJE ZADANIE: Napisz pętlę for, która przejdzie przez listę 'products'.
# Jeśli produkt jest w 'available_products', wypisz: "[Nazwa] jest dostępny".
# W przeciwnym razie wypisz: "[Nazwa] - BRAK W MAGAZYNIE".

for product in products:
    if product in available_products:
        print(f"{product} jest dostępny")
    else:
        print(f"{product} - BRAK W MAGAZYNIE")

# 3. Bonus: Policz ile produktów jest dostępnych
count = len(available_products)
print(f"\nŁącznie dostępnych: {count}")