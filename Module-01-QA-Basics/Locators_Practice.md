## Praktyka Lokatorów: SauceDemo

Poniższa tabela przedstawia wybrane lokatory dla strony [SauceDemo](https://www.saucedemo.com/), które zostaną wykorzystane w późniejszej automatyzacji.

| Element | Typ lokatora | Wartość lokatora | Komentarz |
| :--- | :--- | :--- | :--- |
| **Username Input** | ID | `user-name` | Najlepszy wybór, unikalne ID. |
| **Password Input** | ID | `password` | Unikalne ID. |
| **Login Button** | ID | `login-button` | Unikalne ID. |
| **Error Message** | Data-test | `error` | Atrybut dedykowany pod testy. |

---

### Jak sprawdzić lokator w DevTools?
Aby upewnić się, że powyższe lokatory są poprawne, używam konsoli przeglądarki:
* Dla ID/CSS: `document.querySelector('#user-name')`
* Dla data-test: `document.querySelector('[data-test="error"]')`

