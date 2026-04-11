# 1. Definicja funkcji
def validate_error_message(actual_message, expected_message):
    """
    Funkcja porównuje komunikat wyświetlony na stronie z oczekiwanym.
    """
    if actual_message == expected_message:
        print("✅ TEST PASSED: Komunikat jest poprawny.")
    else:
        print(f"❌ TEST FAILED: Oczekiwano '{expected_message}', ale otrzymano '{actual_message}'")

# 2. Symulacja testu (Wywołanie funkcji)
# Scenariusz: Logowanie zablokowanego użytkownika
error_on_page = "Epic sadface: Sorry, this user has been locked out."
expected_error = "Epic sadface: Sorry, this user has been locked out."

validate_error_message(error_on_page, expected_error)

# 3. ZADANIE: 
# Wywołaj funkcję ponownie, ale tym razem podaj błędny 'expected_error', 
# aby zasymulować sytuację, w której test znajduje błąd.

expected_error = "Epic sadface: Sorry, this user has been locked."
validate_error_message(error_on_page, expected_error)