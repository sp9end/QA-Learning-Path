## Praktyka Lokatorów: SauceDemo

Poniższa tabela przedstawia wybrane lokatory dla strony [SauceDemo](https://www.saucedemo.com/), które zostaną wykorzystane w późniejszej automatyzacji.

| Element | Typ lokatora | Wartość lokatora | Komentarz |
| :--- | :--- | :--- | :--- |
| **Username Input** | ID | `user-name` | Najlepszy wybór, unikalne ID. |
| **Password Input** | ID | `password` | Unikalne ID. |
| **Login Button** | ID | `login-button` | Unikalne ID. |
| **Error Message** | Data-test | `[data-test="error"]` | Atrybut dedykowany pod testy. |
| **First Inventory Item** | CSS | `.inventory_item` | Znajduje pierwszy element na liście. |
| **Shopping Cart** | ID | `shopping_cart_container` | Kontener ikony koszyka. |

---

### Jak sprawdzić lokator w DevTools?
Aby upewnić się, że powyższe lokatory są poprawne, używam konsoli przeglądarki:
* Dla ID/CSS: `document.querySelector('#user-name')`
* Dla data-test: `document.querySelector('[data-test="error"]')`
* Dla CSS: `document.querySelectorAll('.inventory_item')`


