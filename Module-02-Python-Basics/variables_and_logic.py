# 1. Definicja danych testowych
correct_username = "standard_user"
correct_password = "secret_sauce"

# 2. Symulacja wpisanych danych
input_username = "standard_user"
input_password = "secret_sauce"

# 3. Logika testowa (Instrukcja warunkowa)
print(f"Checking login for user: {input_username}...")

if input_username == correct_username and input_password == correct_password:
    print("Test Passed: Login successful!")
else:
    # To jest nasz "Actual Result" w kodzie
    print("Test Failed: Invalid credentials or error message displayed.")

# 4. Prosta asercja
# Asercja to twardy warunek. Jeśli nie jest spełniony, skrypt wyrzuci błąd.
assert input_username == correct_username, "Username mismatch!"
print("Assertion check complete.")